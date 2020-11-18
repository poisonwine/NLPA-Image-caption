import os
import json
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import jieba


valid_annot = 'data/caption_validation_annotations_20170910.json'
with open(valid_annot,'r') as f:
    valid= json.load(f)

valid_test = 'valid_test/index3.json'
with open(valid_test,'r') as f:
    test =json.load(f)
index1_test = []
images = []
name = []
for caption in test:
    cap =caption['caption']
    img_name = caption['image_id'].split('.')[0]
    name.append(caption['image_id'])
    index1_test.append({'caption':cap,'image_id':img_name})
    image_hash = int(int(hashlib.sha256(img_name).hexdigest(), 16) % sys.maxint)
    images.append({'file_name':img_name,'id':image_hash})
print(cap)
#print(name)
annotations = []
for i,image in enumerate(valid):
    image_id = image['image_id']
    if image_id in name:
        hash_id = int(int(hashlib.sha256(image_id.split('.')[0]).hexdigest(), 16) % sys.maxint)
        for cap in image['caption']:
            seglist= jieba.cut(cap,cut_all=False)
            c = ' '.join(seglist)
            print(c)
            annotation = {'caption':c,'image_id':hash_id}
            annotations.append(annotation)
#print(len(annotations))
new_image=[]
for i,a in enumerate(annotations):
    #x= {'caption':a['caption'],'id':i+1,'image_id':a['image_id']}
    a['id'] = i+1
    image_name = a['image_id']
    for image in images:
        if image_name == image['id']:
            new_image.append(image)
new_image2=[]
for i in range(3000):
    new_image2.append(new_image[5*i])

info = {
    "contributor": "Ydy",
    "description": "CaptionEval",
    "url": "https://github.com/AIChallenger/AI_Challenger.git",
    "version": "1",
    "year": 2017
  }
lisence =  [{"url": "https://challenger.ai"}]
type = "captions"


str1 = json.dumps(index1_test,indent=4,ensure_ascii=False, encoding='utf-8')
with open(os.path.join('valid_test','index3_test.json'),'w') as f:
    f.write(str1)

reference = {'annotations':annotations,
             'images':new_image2,
             'info':info,
             'licenses':lisence,
             'type':type}
str2 = json.dumps(reference,indent=4)
with open(os.path.join('valid_test','ref.json'),'w') as f:
    f.write(str2)

with open('data/id_to_words.json','r') as f:
    s=json.load(f)

print(s.keys())