"""
One-time setup: download 20 travel/nature background images from Pexels.
Requires your Pexels API key (free at pexels.com/api).
Run: python3 setup_assets.py YOUR_PEXELS_API_KEY
Images saved to assets/images/ — commit them to the repo.
"""

import io
import sys
import time
from pathlib import Path

import requests
from PIL import Image

OUTPUT_DIR = Path("assets/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SEARCHES = [
    "scottish highlands",
    "coastal cliffs",
    "country cottage",
    "atlantic coast",
    "ancient forest",
    "remote island",
    "moorland sunrise",
    "boutique hotel",
    "cobblestone village",
    "waterfall gorge",
    "mountain lake",
    "fishing harbour",
    "vineyard hills",
    "lighthouse storm",
    "bluebell woodland",
    "mountain pass",
    "stone farmhouse",
    "wildflower meadow",
    "sea stack ocean",
    "misty lake forest",
]


def fetch_pexels(query: str, filename: str, api_key: str, width: int = 1920, height: int = 1080) -> bool:
    try:
        print(f"  Fetching: {filename} ({query})...")
        resp = requests.get(
            "https://api.pexels.com/v1/search",
            headers={"Authorization": api_key},
            params={"query": query, "per_page": 1, "orientation": "landscape"},
            timeout=15,
        )
        resp.raise_for_status()
        photos = resp.json().get("photos", [])
        if not photos:
            print(f"  No results for: {query}")
            return False
        img_url = photos[0]["src"]["original"]
        img_resp = requests.get(img_url, timeout=30)
        img_resp.raise_for_status()
        img = Image.open(io.BytesIO(img_resp.content)).convert("RGB").resize((width, height))
        out_path = OUTPUT_DIR / filename
        img.save(str(out_path), "JPEG", quality=90)
        print(f"  Saved: {out_path} ({out_path.stat().st_size // 1024} KB)")
        return True
    except Exception as e:
        print(f"  FAILED {filename}: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 setup_assets.py YOUR_PEXELS_API_KEY")
        print("Get a free key at: pexels.com/api")
        sys.exit(1)

    api_key = sys.argv[1]
    print(f"Downloading {len(SEARCHES)} background images from Pexels...")
    print(f"Output: {OUTPUT_DIR.resolve()}\n")

    success = 0
    for i, query in enumerate(SEARCHES):
        filename = f"bg_{i+1:02d}.jpg"
        if (OUTPUT_DIR / filename).exists():
            print(f"  Skipping {filename} (already exists)")
            success += 1
            continue
        ok = fetch_pexels(query, filename, api_key)
        if ok:
            success += 1
        time.sleep(0.3)

    print(f"\nDone: {success}/{len(SEARCHES)} images saved to {OUTPUT_DIR}")
    print("\nNext steps:")
    print("  git add assets/images/")
    print("  git commit -m 'add: background images for video slides'")
    print("  git push origin main")


if __name__ == "__main__":
    main()
