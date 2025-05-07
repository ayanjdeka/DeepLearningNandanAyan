import os
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

def generate_dummy_images(class_name, output_dir, count=50):
    os.makedirs(output_dir, exist_ok=True)
    for i in tqdm(range(count), desc=f"Generating {class_name}"):
        img = Image.new('RGB', (256, 256), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        text = f"{class_name} #{i}"
        draw.text((20, 110), text, fill=(0, 0, 0))
        img_path = os.path.join(output_dir, f"{class_name}_{i:03}.png")
        img.save(img_path)

# Output folders
generate_dummy_images("positive", "../webapp/static/generated_images/positive")
generate_dummy_images("negative", "../webapp/static/generated_images/negative")

print("[INFO] Dummy image generation complete.")
