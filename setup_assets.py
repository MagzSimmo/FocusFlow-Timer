"""
One-time setup: download 20 free travel/nature background images from Unsplash.
No API key needed. Run once locally: python3 setup_assets.py
Images saved to assets/images/ — commit them to the repo.
"""

import io
import time
from pathlib import Path

import requests
from PIL import Image

OUTPUT_DIR = Path("assets/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Unsplash Source keywords — each returns a different relevant photo
SEARCHES = [
    "scottish-highlands",
    "coastal-cliffs",
    "country-cottage",
    "atlantic-coast",
    "ancient-forest",
    "remote-island",
    "moorland-sunrise",
    "boutique-hotel",
    "cobblestone-village",
    "waterfall-gorge",
    "mountain-loch",
    "fishing-harbour",
    "vineyard-hills",
    "lighthouse-stormy",
    "bluebell-woodland",
    "mountain-pass",
    "stone-farmhouse",
    "wildflower-meadow",
    "sea-stack-ocean",
    "misty-lake-forest",
]


def fetch_image(keywords: str, filename: str, width: int = 1920, height: int = 1080) -> bool:
    """Download a free photo from Unsplash Source."""
    url = f"https://source.unsplash.com/{width}x{height}/?{keywords},landscape,nature"
    try:
        print(f"  Fetching: {filename} ({keywords})...")
        resp = requests.get(url, timeout=30, allow_redirects=True)
        resp.raise_for_status()
        img = Image.open(io.BytesIO(resp.content)).convert("RGB")
        out_path = OUTPUT_DIR / filename
        img.save(str(out_path), "JPEG", quality=90)
        print(f"  Saved: {out_path} ({out_path.stat().st_size // 1024} KB)")
        return True
    except Exception as e:
        print(f"  FAILED {filename}: {e}")
        return False


def main():
    print(f"Downloading {len(SEARCHES)} background images from Unsplash...")
    print(f"Output: {OUTPUT_DIR.resolve()}\n")

    success = 0
    for i, keywords in enumerate(SEARCHES):
        filename = f"bg_{i+1:02d}.jpg"
        if (OUTPUT_DIR / filename).exists():
            print(f"  Skipping {filename} (already exists)")
            success += 1
            continue
        ok = fetch_image(keywords, filename)
        if ok:
            success += 1
        time.sleep(0.5)

    print(f"\nDone: {success}/{len(SEARCHES)} images saved to {OUTPUT_DIR}")
    print("\nNext steps:")
    print("  git add assets/images/")
    print("  git commit -m 'add: background images for video slides'")
    print("  git push origin main")


if __name__ == "__main__":
    main()
