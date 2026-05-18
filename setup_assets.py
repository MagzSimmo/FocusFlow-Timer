"""
One-time setup: generate 20 branded background images for video slides and thumbnails.
Uses Pollinations.ai (free, no API key needed) with Flux image model.
Run once locally: python setup_assets.py
Images saved to assets/images/ — commit them to the repo.
"""

import time
from pathlib import Path

import requests
from PIL import Image, ImageDraw
import io

OUTPUT_DIR = Path("assets/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS = [
    "dramatic coastal cliffs at golden hour, dark navy tones, no people, cinematic",
    "misty Scottish highlands mountains, moody atmosphere, deep blue tones, no people",
    "ancient stone cottage in rolling green hills, dusk light, no people",
    "rugged Atlantic coastline waves crashing, dark stormy sky, no text",
    "dense ancient forest path with dappled light, deep green and navy, no people",
    "remote island aerial view, turquoise water, dramatic clouds, no people",
    "windswept moorland at sunrise, orange and navy sky, no people, cinematic",
    "luxury boutique hotel exterior at twilight, warm lights, no people",
    "narrow cobblestone village street, golden evening light, no people",
    "wild river gorge with waterfalls, lush green, dark tones, no people",
    "dramatic mountain loch reflection, navy and silver tones, no people",
    "coastal fishing harbour at dawn, mist, dark moody tones, no people",
    "rolling vineyard hills at sunset, warm amber tones, no people",
    "remote lighthouse on rocky headland, stormy sea, dramatic sky",
    "ancient woodland with bluebells, dappled light, deep green, no people",
    "mountain pass with dramatic cloud shadows, navy tones, no people",
    "traditional stone farmhouse in winter landscape, muted tones, no people",
    "wild meadow with wildflowers, golden hour, bokeh, no people",
    "dramatic sea stack rock formations, navy ocean, no people, cinematic",
    "lakeside forest at dawn, mist on water, deep blue and green tones",
]

def generate_image(prompt: str, filename: str, width: int = 1920, height: int = 1080) -> bool:
    """Download an AI-generated image from Pollinations.ai."""
    import urllib.parse
    encoded = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width={width}&height={height}&nologo=true&seed={hash(prompt) % 10000}"
    
    try:
        print(f"  Generating: {filename}...")
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        
        img = Image.open(io.BytesIO(resp.content))
        out_path = OUTPUT_DIR / filename
        img.save(str(out_path), "JPEG", quality=90)
        print(f"  Saved: {out_path} ({out_path.stat().st_size // 1024} KB)")
        return True
    except Exception as e:
        print(f"  FAILED {filename}: {e}")
        return False


def main():
    print(f"Generating {len(PROMPTS)} background images...")
    print(f"Output: {OUTPUT_DIR.resolve()}\n")
    
    success = 0
    for i, prompt in enumerate(PROMPTS):
        filename = f"bg_{i+1:02d}.jpg"
        if (OUTPUT_DIR / filename).exists():
            print(f"  Skipping {filename} (already exists)")
            success += 1
            continue
        
        ok = generate_image(prompt, filename)
        if ok:
            success += 1
        time.sleep(1)  # be polite to the free API
    
    print(f"\nDone: {success}/{len(PROMPTS)} images saved to {OUTPUT_DIR}")
    print("\nNext steps:")
    print("  git add assets/images/")
    print("  git commit -m 'add: AI-generated background images'")
    print("  git push origin main")


if __name__ == "__main__":
    main()
