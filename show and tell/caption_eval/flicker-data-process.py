import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import jieba
import hashlib

def process_reference_ch(test_path):
    #test_path = 'data/flickr8k_test_captions.txt'
    images = []
    annotations = []
    with open(test_path,'r') as f:
        names = []
        id = 1
        for line in f.readlines():
            image_name=line.split('#')[0].split('.')[0]
            image_hash = int(int(hashlib.sha256(image_name).hexdigest(), 16) % sys.maxint)
            if image_name not in names:
                names.append(image_name)
            cap = line.split(' ')[-1].strip('\n').strip('\r')
            cap = cap.decode('utf-8')
            seglist = jieba.cut(cap, cut_all=False)
            c = ' '.join(seglist)
            print(image_name, c, image_hash)
            ann = {'caption':c, 'id':id, 'image_id':image_hash}
            annotations.append(ann)
            id +=1
    print(names)

    for name in names:
        image_hash = int(int(hashlib.sha256(name).hexdigest(), 16) % sys.maxint)
        img = {'file_name': name, 'id': image_hash}
        images.append(img)

    info = {
        "contributor": "Ydy",
        "description": "CaptionEval_flicker",
        "version": "1",
        "year": 2020
      }
    lisence =  [{"url": "https://challenger.ai"}]
    type = "captions"
    reference = {'annotations':annotations,
                 'images':images,
                 'info':info,
                 'licenses':lisence,
                 'type':type}
    str1 = json.dumps(reference,indent=4)
    with open(os.path.join('valid_test','flicker_ref_chinese.json'),'w') as f:
        f.write(str1)
    return names

path = 'data/flickr8k_test_captions.txt'
names=process_reference_ch(path)

def process_ficker_chinese(test_data,names):
    #test_data = 'valid_test/flicker_index3.json'
    with open(test_data,'r') as f:
        captions = json.load(f)
    new_cap=[]
    for caption in captions:
        image_name = caption['image_id'].split('.')[0]
        #hash_id = int(int(hashlib.sha256(image_name).hexdigest(), 16) % sys.maxint)
        if image_name in names:
            c = {'caption':caption['caption'],'image_id': image_name}
            new_cap.append(c)
    print(len(new_cap))
    str2 = json.dumps(new_cap, indent=4, ensure_ascii=False, encoding='utf-8')
    with open(os.path.join('valid_test','new_flicker3.json'),'w') as f:
        f.write(str2)
#process_ficker_chinese()
