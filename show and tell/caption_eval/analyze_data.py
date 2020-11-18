# -*- coding: utf-8 -*-
import json
import os

import jieba#引用中文分词组件
from tqdm import tqdm#终端进度条工具


if __name__ == '__main__':
    print('Calculating the maximum length among all the captions')#计算所有描述中的最大长度
    annotations_path = 'data/caption_train_annotations_20170902.json'

    with open(annotations_path, 'r') as f:#只读打开文件
        samples = json.load(f)#读取json信息
    print(samples[0])
    max_len = 0
    for sample in tqdm(samples):
        caption = sample['caption']#读取caption键对应值
        for c in caption:
            seg_list = jieba.cut(c, cut_all=True)#将字符串分词
            length = sum(1 for item in seg_list)#计算该句描述中的分词数
            if length > max_len:
                max_len = length
    print('max_len: ' + str(max_len))#输出所有描述中的最大长度
