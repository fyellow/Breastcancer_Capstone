import os
import random
from shutil import copyfile

# Define the paths to your image files
data_dir = 'E:/Capstone/train_2-20230321T024417Z-001'
train_dir = 'E:/Capstone/train_dir'
val_dir = 'E:/Capstone/val_dir'
test_dir = 'E:/Capstone/test_dir'

# Define the ratio in which you want to split the data
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create the subdirectories for each class and each subset
os.makedirs(os.path.join(train_dir, 'tumor'))
os.makedirs(os.path.join(train_dir, 'no_tumor'))
os.makedirs(os.path.join(val_dir, 'tumor'))
os.makedirs(os.path.join(val_dir, 'no_tumor'))
os.makedirs(os.path.join(test_dir, 'tumor'))
os.makedirs(os.path.join(test_dir, 'no_tumor'))

# Loop through each class (tumor and no tumor) and randomly assign its images to a subset
for class_name in os.listdir(data_dir):
    if class_name == 'tumor':
        class_dir = os.path.join(data_dir, 'tumor')
    elif class_name == 'no_tumor':
        class_dir = os.path.join(data_dir, 'no_tumor')
    else:
        continue
    for file_name in os.listdir(class_dir):
        if file_name.endswith('.bmp'):
            source = os.path.join(class_dir, file_name)
            rand = random.random()
            if rand < train_ratio:
                if class_name == 'tumor':
                    destination = os.path.join(train_dir, 'tumor', file_name)
                else:
                    destination = os.path.join(train_dir, 'no_tumor', file_name)
            elif rand < train_ratio + val_ratio:
                if class_name == 'tumor':
                    destination = os.path.join(val_dir, 'tumor', file_name)
                else:
                    destination = os.path.join(val_dir, 'no_tumor', file_name)
            else:
                if class_name == 'tumor':
                    destination = os.path.join(test_dir, 'tumor', file_name)
                else:
                    destination = os.path.join(test_dir, 'no_tumor', file_name)
            copyfile(source, destination)
