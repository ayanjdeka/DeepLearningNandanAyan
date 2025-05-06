import os
import subprocess
import torch

# Detect CUDA
use_gpu = torch.cuda.is_available()

if not use_gpu:
    raise RuntimeError("CUDA is not available. Please install CUDA-enabled PyTorch.")

# Training settings
gpus = "1"
aug = "ada"
batch = "16"  # You can try 32 if your GPU has enough memory
kimg = "200"  # Fast training (~5–15 min per model)
cfg = "auto"

# Datasets
datasets = {
    "positive": "../datasets/positive.zip",
    "negative": "../datasets/negative.zip"
}
out_base = "../training-runs"

# Train each class
for label, dataset_path in datasets.items():
    outdir = os.path.join(out_base, label)
    print(f"\n[INFO] Training on '{label}' dataset using GPU...")

    cmd = [
        "python", "train.py",
        f"--outdir={outdir}",
        f"--data={dataset_path}",
        f"--gpus={gpus}",
        f"--cfg={cfg}",
        f"--batch={batch}",
        f"--kimg={kimg}",
        f"--aug={aug}"
    ]

    subprocess.run(cmd)
