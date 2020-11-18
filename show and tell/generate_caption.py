# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')
# import the necessary packages
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import pickle
import keras.backend as K
import numpy as np
from keras.preprocessing import sequence
# 从config文件中引入一些参数 包括token最大长度 测试文件夹长度 最优的模型参数
from src.config import max_token_length, test_a_image_folder, best_model
from forward import build_model
import keras
from keras_applications.resnet50 import ResNet50
from keras_preprocessing.image import (load_img,img_to_array)
from keras.models import load_model
from src.config import img_rows, img_cols
import time
from src.config import train_image_folder, valid_image_folder, test_a_image_folder, test_b_image_folder

image_model = ResNet50(include_top=False,
                        weights='imagenet',
                        layers=keras.layers,
                        models=keras.models,
                        utils=keras.utils,
                        pooling='avg',
                        backend=keras.backend)
# model_weights_path = os.path.join('models', best_model)
# print('模型加载中...')
#     # 创建模型
# model = build_model()
#     # 加载模型权重
# model.load_weights(model_weights_path)
# print('模型加载完毕...')
# model.save('caption_model.h5')

def encode_images(image_path):
    encoding={}
    #names储存文件夹中所有的jpg文件名称
    name = image_path.split('/')[-1]
    #输出编码过程
    print('ResNet50提取特征中...')
    #对每个batche进行处理，使用tqdm库显示处理进度
        #使用empty创建一个多维数组
    image_input = np.empty((1,img_rows, img_cols, 3))
    #对于每一张图片
    #keras读取图片，并且将图片调整为224*224
    img = load_img(image_path, target_size=(img_rows, img_cols))
    #将图片转为矩阵
    img_array = img_to_array(img)
    #使用keras内置的preprocess_input进行图片预处理，默认使用caffe模式去均值中心化
    img_array = keras.applications.resnet50.preprocess_input(img_array)

    #将处理后的图片保存到image_input中
    image_input[0] =img_array
    #使用ResNet50网络进行预测，预测结果保存到preds中
    encodes = image_model.predict(image_input)
    encodes = encodes.flatten()
    encoding[name] = encodes
    print('ResNet50提取特征完毕...')

    return encoding,name


def beam_search_predictions(model, image_name, word2idx, idx2word, encoding_test, beam_index=3):
    start = [word2idx["<start>"]]
    start_word = [[start, 0.0]]

    while len(start_word[0][0]) < max_token_length:
        temp = []
        for s in start_word:
            # 对序列进行填充的预处理，在其后添0，使其序列统一大小为max_token_length
            par_caps = sequence.pad_sequences([s[0]], maxlen=max_token_length, padding='post')
            # 每次取一个图片进行测试
            e = encoding_test[image_name]
            # 使用模型对该图片进行测试
            preds = model.predict([np.array([e]), np.array(par_caps)])
            # 从预测的结果中取前beam_index个
            word_preds = np.argsort(preds[0])[-beam_index:]

            # Getting the top <beam_index>(n) predictions and creating a
            # new list so as to put them via the model again
            # 创建一个新的list结构 将预测出的词和词的概率以组对的形式存储
            for w in word_preds:
                next_cap, prob = s[0][:], s[1]
                next_cap.append(w)
                prob += preds[0][w]
                temp.append([next_cap, prob])
        # 将处理好的预测值赋值回start word
        start_word = temp
        # Sorting according to the probabilities
        # 根据概率排序
        start_word = sorted(start_word, reverse=False, key=lambda l: l[1])
        # Getting the top words
        # 获得最有可能正确的词
        start_word = start_word[-beam_index:]

    start_word = start_word[-1][0]
    # 根据id取出单词
    intermediate_caption = [idx2word[i] for i in start_word]

    final_caption = []
    # 组合成句
    for i in intermediate_caption:
        if i != '<end>':
            final_caption.append(i)
        else:
            break

    final_caption = ''.join(final_caption[1:])
    return final_caption

def generate_caption(img_path):

    channel = 3
    # 设置模型权重的地址
    model_weights_path = os.path.join('models', best_model)
    print('模型加载中...')
    # 创建模型
    model = build_model()
    # 加载模型权重
    model.load_weights(model_weights_path)
    print('模型加载完毕...')
    #model = load_model('caption_model.h5')
    # print(model.summary())
    #加载语料库
    vocab = pickle.load(open('data/vocab_train.p', 'rb'))
    # 将word转化为数字  方便输入网络 进行预测
    idx2word = sorted(vocab)
    word2idx = dict(zip(idx2word, range(len(vocab))))
    print('语料库加载完毕...')
    encoding, name = encode_images(img_path)
    image_name = name
    image_input = np.zeros((1, 2048))
    image_input[0] = encoding[name]
    # 获取图片的名称
    filename = os.path.join(test_a_image_folder, image_name)
    # print('Start processing image: {}'.format(filename))
    # 设置不同的预测参数，并放到beam_search_predictions中进行预测
    print('描述的图片为:', name)
    sentences=[]
    candidate1 = beam_search_predictions(model, image_name, word2idx, idx2word, encoding, beam_index=1)
    print('Beam Search, k=1:', candidate1)
    sentences.append(candidate1)

    # candidate2 = beam_search_predictions(model, image_name, word2idx, idx2word, encoding, beam_index=3)
    # print('Beam Search, k=3:', candidate2)
    # sentences.append(candidate2)
    #
    # candidate3 = beam_search_predictions(model, image_name, word2idx, idx2word, encoding, beam_index=5)
    # print('Beam Search, k=5:', candidate3)
    # sentences.append(candidate3)

    K.clear_session()
    return sentences

# if __name__ =='__main__':
start = time.time()
image_path = 'images/image_7.jpg'
sentence = generate_caption(image_path)
print(time.time()-start)