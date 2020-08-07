
###1!!!!   remobe voc devkit
import xml.etree.ElementTree as ET
import os
from os import getcwd

sets=[('2020_relarge', 'train')]

# ../coco/images/train2017/000000109622.jpg  # image
# ../coco/labels/train2017/000000109622.txt  # label


# print(sets[0][0],sets[0][1])

classes = ["cell phone","person"]



import random
 
"""
随机按比例拆分数据
"""
 
def split(all_list, shuffle=False, ratio=0.8):
    num = len(all_list)
    offset = int(num * ratio)
    if num == 0 or offset < 1:
        return [], all_list
    if shuffle:
        random.shuffle(all_list)  # 列表随机排序
    train = all_list[:offset]
    test = all_list[offset:]
    return train, test


# original generate code (no remove vocdevkit)
wd = getcwd()
remote_path="/media/daniel/D/ycc/dataset/cellphone/"

for year, image_set in sets:
    image_path = open('VOC%s/%s_%s.txt'%(year,year, image_set)).read().strip().split()
    list_file_train = open('VOC%s/VOC%s_train.txt'%(year,year), 'w')
    list_file_valid = open('VOC%s/VOC%s_valid.txt'%(year,year), 'w')


    traindatas, testdatas = split(image_path, shuffle=True, ratio=0.7)  
    #按照0.6进行划分数据

    for tr_data in traindatas:
        list_file_train.write(tr_data+"\n")
    list_file_train.close()

    for te_data in testdatas:
        list_file_valid.write(te_data+"\n")
    list_file_valid.close()





