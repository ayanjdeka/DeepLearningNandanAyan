# Synthetic Medical Image Generation and Evaluation with StyleGAN2-ADA

This project generates synthetic chest X-ray images using StyleGAN2-ADA and evaluates their diagnostic utility through a web interface.
## IT IS IMPORTANT TO NOTE THAT AT LEAST ONE GPU IS NEEDED ON YOUR PERSONAL MACHINE FOR THIS TO RUN
## Steps to reproduce the project
1. Download the data from this link https://www.kaggle.com/datasets/andyczhao/covidx-cxr2/versions/1
2. Run preprocess.py on the data
3. clone [stylegan2](https://github.com/NVlabs/stylegan2-ada-pytorch/tree/d72cc7d041b42ec8e806021a205ed9349f87c6a4)
4. cd into stlegan2-ada-pytorch and install the requirments in their read me
5. run these two functions, python dataset_tool.py --source=processed_dataset/train/positive --dest=datasets/positive.zip and python dataset_tool.py --source=processed_dataset/train/negative --dest=datasets/negative.zip (note that none of these datasets are within the repository since the files were too large)
6. run this in the terminal: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
7. copy the train_auto.py into the stlegan2-ada-pytorch directory and run the file to train the model with the dataset
8. for this part, we had to generate dummy images since my machine could not train long enough for a snapcshot (even though data as found in my training runs file), but if a pkl is found in your training runs folder, run the functions python generate.py --outdir=generated_images/normal --trunc=1 --seeds=0-99 --network=../training-runs/negative/network-snapshot-<iteration>.pkl to generate images based on the trained model
9. cd into the webapp part of this repository, and run app
10. Get a professional and use your intution to see what is negative or positive regarding covid and lungs, and continue until you want to end
11. The final statistics should be displayed at the end 