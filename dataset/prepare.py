import os
import shutil
import random

# This script assumes dataset is downloaded and unzipped in a folder named 'PlantVillage'
# under the dataset directory. It will organize images into train/val/test splits as
# described in project requirements.

SOURCE_DIR = os.path.join(os.path.dirname(__file__), 'PlantVillage')
TARGET_DIR = os.path.join(os.path.dirname(__file__), 'processed')

CLASSES = [
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Corn___Cercospora_leaf_spot_Gray_leaf_spot',
    'Corn___Common_rust',
    'Corn___Northern_Leaf_Blight',
    'Corn___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
]

SPLITS = {'train': 0.7, 'val': 0.15, 'test': 0.15}


def prepare():
    if not os.path.isdir(SOURCE_DIR):
        print(f"Source directory {SOURCE_DIR} does not exist. Please download PlantVillage and unzip.")
        return
    os.makedirs(TARGET_DIR, exist_ok=True)
    for split in SPLITS:
        for cls in CLASSES:
            os.makedirs(os.path.join(TARGET_DIR, split, cls), exist_ok=True)
    
    for cls in CLASSES:
        class_dir = os.path.join(SOURCE_DIR, cls)
        if not os.path.isdir(class_dir):
            print(f"Class directory missing: {class_dir}")
            continue
        images = [f for f in os.listdir(class_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
        random.shuffle(images)
        n = len(images)
        i = 0
        for split, frac in SPLITS.items():
            count = int(frac * n)
            for img in images[i:i+count]:
                src = os.path.join(class_dir, img)
                dst = os.path.join(TARGET_DIR, split, cls, img)
                shutil.copyfile(src, dst)
            i += count
    print("Dataset preparation complete."
)

if __name__ == '__main__':
    prepare()
