import os
import random
from PIL import Image
from tqdm import tqdm

# Configuration
base_path = r"C:\Users\ayanj\Projects\DeepLearningFinal"
image_size = (256, 256)
sample_fraction = 1.0
output_base = os.path.join(base_path, "processed_subset")

# Ensure output dirs exist
for split in ["train", "test"]:
    for label in ["positive", "negative"]:
        os.makedirs(os.path.join(output_base, split, label), exist_ok=True)

def preprocess_split(split):
    img_dir = os.path.join(base_path, split)
    txt_path = os.path.join(base_path, f"{split}.txt")

    # Read and sample lines
    with open(txt_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    random.shuffle(lines)
    sample_size = int(len(lines) * sample_fraction)
    sampled = lines[:sample_size]

    print(f"Processing {split}: using {sample_size} out of {len(lines)} lines...")

    for line in tqdm(sampled, desc=f"Preprocessing {split}"):
        parts = line.split()
        if len(parts) < 4:
            continue

        filename = parts[1]
        label = parts[2].lower()
        src_path = os.path.join(img_dir, filename)
        dst_path = os.path.join(output_base, split, label, filename)

        if not os.path.exists(src_path):
            print(f"Missing file: {filename}")
            continue

        try:
            with Image.open(src_path) as img:
                img = img.convert("RGB")
                img = img.resize(image_size)
                img.save(dst_path)
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

# Run both splits
preprocess_split("train")
preprocess_split("test")
