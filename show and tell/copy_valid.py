import os
import shutil
import random
path1 = 'data/ai_challenger_caption_validation_20170910/caption_validation_images_20170910'
path2 = 'data/ai_challenger_caption_validation_20170910/10000_test'
if not os.path.exists(path2):
    os.makedirs(path2)
ids = os.listdir(path1)
random.shuffle(ids)
new_ids = ids[:10000]
print(ids)
for id in new_ids:
    img = os.path.join(path1, id)
    shutil.copyfile(img, os.path.join(path2,id))