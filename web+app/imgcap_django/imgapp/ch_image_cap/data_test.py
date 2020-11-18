import sys
sys.path.insert(0, 'src')
import json
import pickle
import zipfile
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

import jieba
import keras
import numpy as np
from keras_applications.resnet50 import ResNet50
from keras_applications.resnet import ResNet101
from keras_preprocessing.image import (load_img,img_to_array)
from tqdm import tqdm

from src.config import img_rows, img_cols
from src.config import start_word, stop_word, unknown_word
from src.config import train_annotations_filename
from src.config import train_folder, valid_folder, test_a_folder, test_b_folder
from src.config import train_image_folder, valid_image_folder, test_a_image_folder, test_b_image_folder
from src.config import valid_annotations_filename


annotations_path = os.path.join(train_folder, train_annotations_filename)
#读取json格式的标注文件
with open(annotations_path, 'r') as f:
    annotations = json.load(f)
print(len(annotations))
