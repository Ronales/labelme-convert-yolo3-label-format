
###1!!!!   remobe voc devkit
import xml.etree.ElementTree as ET
import os
from os import getcwd

sets=[('2020_1', 'train')]

# ../coco/images/train2017/000000109622.jpg  # image
# ../coco/labels/train2017/000000109622.txt  # label


# print(sets[0][0],sets[0][1])

classes = ["cell phone","person"]

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id, list_file):
    in_file = open('VOC%s/Annotations/%s.xml'%(year, image_id))
    out_file = open('VOC%s/labels/%s.txt'%(year, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        #difficult = obj.find('difficult').text
        cls = obj.find('name').text        
        # if cls not in classes or int(difficult)==1:
        #     continue
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        # list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


for year, image_set in sets:
    main_id=os.listdir('VOC%s/Annotations/'%(year))
    # print(main_id)
    if not os.path.exists('VOC%s/ImageSets/Main/%s.txt'%(year, image_set)):
        os.makedirs('VOC%s/ImageSets/Main/'%(year))
    main_txt_file=open('VOC%s/ImageSets/Main/%s.txt'%(year, image_set),'w')
    for id_index in main_id:
        main_txt_file.write(id_index[:-4])
        main_txt_file.write("\n")
    main_txt_file.close()

    

# original generate code (no remove vocdevkit)
wd = getcwd()
remote_path="/media/daniel/D/ycc/dataset/cellphone/"

for year, image_set in sets:
    if not os.path.exists('VOC%s/labels/'%(year)):
        os.makedirs('VOC%s/labels/'%(year))

    image_ids = open('VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('VOC%s/%s_%s.txt'%(year,year, image_set), 'w')
    for image_id in image_ids:
        list_file.write(remote_path+'VOC%s/images/%s/%s.jpg'%(year,year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()







###2!!!!   no remove vocdevkit



# import xml.etree.ElementTree as ET
# import os
# from os import getcwd

# sets=[('2007', 'train')]

# # print(sets[0][0],sets[0][1])

# classes = ["cell phone","person"]

# def convert(size, box):
#     dw = 1./(size[0])
#     dh = 1./(size[1])
#     x = (box[0] + box[1])/2.0 - 1
#     y = (box[2] + box[3])/2.0 - 1
#     w = box[1] - box[0]
#     h = box[3] - box[2]
#     x = x*dw
#     w = w*dw
#     y = y*dh
#     h = h*dh
#     return (x,y,w,h)

# def convert_annotation(year, image_id, list_file):
#     in_file = open('VOC%s/Annotations/%s.xml'%(year, image_id))
#     out_file = open('VOCdevkit/VOC%s/labels/%s.txt'%(year, image_id), 'w')
#     tree=ET.parse(in_file)
#     root = tree.getroot()
#     size = root.find('size')
#     w = int(size.find('width').text)
#     h = int(size.find('height').text)

#     for obj in root.iter('object'):
#         #difficult = obj.find('difficult').text
#         cls = obj.find('name').text        
#         # if cls not in classes or int(difficult)==1:
#         #     continue
#         if cls not in classes:
#             continue
#         cls_id = classes.index(cls)
#         xmlbox = obj.find('bndbox')
#         b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
#         bb = convert((w,h), b)
#         # list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
#         out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


# for year, image_set in sets:
#     main_id=os.listdir('VOC%s/Annotations/'%(year))
#     # print(main_id)
#     if not os.path.exists('VOC%s/ImageSets/Main/%s.txt'%(year, image_set)):
#         os.makedirs('VOC%s/ImageSets/Main/'%(year))
#     main_txt_file=open('VOC%s/ImageSets/Main/%s.txt'%(year, image_set),'w')
#     for id_index in main_id:
#         main_txt_file.write(id_index[:-4])
#         main_txt_file.write("\n")
#     main_txt_file.close()

    

# # original generate code (no remove vocdevkit)
# wd = getcwd()
# for year, image_set in sets:
#     if not os.path.exists('VOCdevkit/VOC%s/labels/'%(year)):
#         os.makedirs('VOCdevkit/VOC%s/labels/'%(year))

#     image_ids = open('VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
#     list_file = open('%s_%s.txt'%(year, image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
#         convert_annotation(year, image_id, list_file)
#         list_file.write('\n')
#     list_file.close()