"""Generate a branded 1280x720 YouTube thumbnail."""

from __future__ import annotations

import io
from pathlib import Path

import google.generativeai as genai
from PIL import Image, ImageDraw, ImageFont

import config


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype(config.FONT_PATH, size)
    except (IOError, OSError):
        return ImageFont.load_default()


def _wrap_text(text: str, font, max_width: int, draw: ImageDraw.ImageDraw) -> str:
    words = text.split()
    lines, current = [], []
    for word in words:
        test = " ".join(current + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] > max_width and current:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines)


def _gemini_background(title: str, api_key: str) -> Image.Image | None:
    try:
        genai.configure(api_key=api_key)
        imagen = genai.ImageGenerationModel(config.GEMINI_IMAGE_MODEL)
        prompt = (
            f"Bold professional thumbnail background for a B2B sales YouTube video: {title}. "
            "Dark navy background, dramatic lighting, abstract business concept, "
            "no text, no people, suitable for YouTube thumbnail."
        )
        result = imagen.generate_images(prompt=prompt, number_of_images=1)
        if result.images:
            img_bytes = result.images[0]._image_bytes
            return Image.open(io.BytesIO(img_bytes)).resize(config.THUMBNAIL_RESOLUTION)
    except Exception as e:
        print(f"[thumbnail] Gemini image failed: {e}. Using solid background.")
    return None


def generate_thumbnail(
    title: str,
    output_path: Path,
    gemini_key: str | None = None,
) -> Path:
    """
    Create a 1280x720 JPEG thumbnail.
    Uses Gemini for background if a key is provided, otherwise Pillow-only.
    """
    w, h = config.THUMBNAIL_RESOLUTION

    bg = None
    if gemini_key and config.IMAGES_PER_VIDEO > 0:
        bg = _gemini_background(title, gemini_key)

    if bg is None:
        bg = Image.new("RGB", (w, h), color=config.BACKGROUND_COLOR)
        draw = ImageDraw.Draw(bg)
        # Left accent stripe
        draw.rectangle([(0, 0), (12, h)], fill=config.ACCENT_COLOR)
        # Top accent stripe
        draw.rectangle([(0, 0), (w, 8)], fill=config.ACCENT_COLOR)

    # Dark overlay for text legibility
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 140))
    bg = Image.alpha_composite(bg.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(bg)

    title_font = _load_font(90)
    brand_font = _load_font(40)

    pad = 60
    max_text_width = w - 2 * pad

    wrapped = _wrap_text(title, title_font, max_text_width, draw)
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=title_font, spacing=12)
    text_h = bbox[3] - bbox[1]

    # Centre title vertically, shifted slightly up
    start_y = max(pad, (h - text_h) // 2 - 30)
    draw.multiline_text(
        (pad, start_y),
        wrapped,
        font=title_font,
        fill=config.TEXT_COLOR,
        spacing=12,
    )

    # Channel name bottom-left
    draw.text(
        (pad, h - pad - 40),
        config.CHANNEL_NAME,
        font=brand_font,
        fill=config.ACCENT_COLOR,
    )

    # Logo bottom-right
    logo_path = Path(config.LOGO_PATH)
    if logo_path.exists():
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail((180, 60))
            bg.paste(logo, (w - logo.width - pad, h - logo.height - pad // 2), logo)
        except Exception:
            pass

    output_path.parent.mkdir(parents=True, exist_ok=True)
    bg.save(str(output_path), "JPEG", quality=92)

    # Verify size < 2 MB (YouTube limit)
    size_mb = output_path.stat().st_size / (1024 * 1024)
    if size_mb > 2:
        bg.save(str(output_path), "JPEG", quality=75)

    return output_path
