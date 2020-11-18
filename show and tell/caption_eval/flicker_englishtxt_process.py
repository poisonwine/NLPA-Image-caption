import os
import json
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def process_reference_english(test_path):
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
            cap = line.split('#')[-1][2:].strip('\n').strip('\r').strip(' .')
            cap = cap.decode('utf-8')
            print(image_name, cap, image_hash)
            ann = {'caption':cap, 'id':id, 'image_id':image_hash}
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
    with open(os.path.join('valid_test','flicker_ref_english.json'),'w') as f:
        f.write(str1)
    return names

path = 'data/flicker/flickr8kenc.caption.txt'
names = process_reference_english(path)
print(names)