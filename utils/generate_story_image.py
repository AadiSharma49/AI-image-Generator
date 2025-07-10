from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import textwrap
import os
import uuid
from dotenv import load_dotenv

# Load API key from secrets
load_dotenv("config/secrets.env")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def fetch_images_by_topic(topic, count=3):
    """Fetch multiple image URLs for a topic using Pexels API."""
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": topic, "per_page": count}
    
    try:
        response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [photo["src"]["large2x"] for photo in data.get("photos", [])]
    except Exception as e:
        print(f"[❌] Error fetching images: {e}")
        return []

def create_story_images(topic, output_dir="static/assets", count=3):
    os.makedirs(output_dir, exist_ok=True)

    # Font paths and fallback
    font_path = "utils/fonts/OpenSans-Bold.ttf"
    if not os.path.exists(font_path):
        font_path = "C:/Windows/Fonts/arialbd.ttf" if os.name == "nt" else "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    
    try:
        font = ImageFont.truetype(font_path, 70)
    except Exception as e:
        print(f"[❌] Font load failed: {e}")
        font = ImageFont.load_default()

    image_urls = fetch_images_by_topic(topic, count)
    generated_files = []

    for url in image_urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            image_data = response.content
            image = Image.open(BytesIO(image_data)).convert("RGBA").resize((1080, 1920))

            # Add dark overlay
            overlay = Image.new("RGBA", image.size, (0, 0, 0, 120))
            image = Image.alpha_composite(image, overlay)

            draw = ImageDraw.Draw(image)
            lines = textwrap.wrap(topic, width=20)
            total_height = sum(draw.textbbox((0, 0), line, font=font)[3] for line in lines) + (len(lines) - 1) * 20
            y = (image.height - total_height) // 2

            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=font)
                w = bbox[2] - bbox[0]
                draw.text(((image.width - w) / 2, y), line, font=font, fill=(255, 255, 255, 255))
                y += bbox[3] + 20

            filename = f"{uuid.uuid4().hex}.jpg"
            filepath = os.path.join(output_dir, filename)
            image.convert("RGB").save(filepath)
            generated_files.append(filename)
            print(f"[✅] Image saved: {filepath}")

        except Exception as e:
            print(f"[❌] Failed to generate image for URL {url}: {e}")

    return generated_files
