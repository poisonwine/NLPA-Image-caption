import json
import zipfile
from collections import Counter

import jieba
from tqdm import tqdm

from config import *
from utils import ensure_folder


def extract(folder):
    filename = '{}.zip'.format(folder)
    print('Extracting {}...'.format(filename))
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('data')


def create_input_files():
    json_path = 'data/caption_train_annotations_20170902.json'

    # Read JSON
    with open(json_path, 'r') as j:
        samples = json.load(j)

    # Read image paths and captions for each image
    word_freq = Counter()

    for sample in tqdm(samples):
        caption = sample['caption']
        for c in caption:
            seg_list = jieba.cut(c)
            # Update word frequency
            word_freq.update(seg_list)

    # Create word map
    words = [w for w in word_freq.keys() if word_freq[w] > min_word_freq]
    word_map = {k: v + 1 for v, k in enumerate(words)}
    word_map['<unk>'] = len(word_map) + 1
    word_map['<start>'] = len(word_map) + 1
    word_map['<end>'] = len(word_map) + 1
    word_map['<pad>'] = 0
    #word_map = {k:v for k in list(word_map.keys())[:9527] for v in list(word_map.values())[:9527]}
    print(len(word_map))

    print(words[:10])

    # Save word map to a JSON
    with open(os.path.join(data_folder, 'WORDMAP.json'), 'w') as j:
        json.dump(word_map, j)


if __name__ == '__main__':
    # parameters
    ensure_folder('data')

    # if not os.path.isdir(train_image_folder):
    #     extract(train_folder)
    #
    # if not os.path.isdir(valid_image_folder):
    #     extract(valid_folder)

    # if not os.path.isdir(test_a_image_folder):
    #     extract(test_a_folder)
    #
    # if not os.path.isdir(test_b_image_folder):
    #     extract(test_b_folder)

    create_input_files()
