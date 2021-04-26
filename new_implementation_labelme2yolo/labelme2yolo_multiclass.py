# -*- coding: utf-8 -*-

'''
#1、LabelMe JSON format -> YOLO txt format
1-1、 bbox (xyxy)  ->  x(center) y(center) w h

'''

import os
from os import walk, getcwd
from PIL import Image
import json
import cv2

def convert_bbox(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return x,y,w,h
    
def convert_polypoints(size, poly):
    dw = 1./size[0]
    dh = 1./size[1]

    x = poly[0]
    y = poly[1]

    x = x*dw
    y = y*dh
    return x,y


"""-------------------------------------------------------------------""" 

""" Configure Paths"""   
mypath = "./"
outpath = "./"
json_backup ="./json_backup/"

if not os.path.exists(outpath):
    os.makedirs(outpath)


wd = getcwd()
#list_file = open('%s_list.txt'%(wd), 'w')

""" Get input json file list """
json_name_list = []
for file in os.listdir(mypath):
    if file.endswith(".json"):
        json_name_list.append(file)
    
final_dict ={}
""" Process """
for json_name in json_name_list:
    txt_name = json_name.rstrip(".json") + ".txt"
    """ Open input text files """
    txt_path = mypath + json_name
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    
    """ Open output text files """
    txt_outpath = outpath + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "a",encoding='utf-8')

    """ Convert the data to YOLO format """ 
    # lines = txt_file.read().split('\r\n')   #for ubuntu, use "\r\n" instead of "\n"

    temp_dict={}
    anno_list=[]
    data = json.load(txt_file)
    for shape in data['shapes']:   #遍历多个shapes 每个shapes包含标注的信息。点坐标或者bbox四个值
        if shape["shape_type"] == "point":  #xy
            temp_dict[shape["label"]]=shape["points"][0]
    
        if shape["shape_type"] == "rectangle":#xyxy
   
            temp_dict[shape["label"]]=shape["points"]

    img_path = mypath + json_name.split(".")[0] + ".jpg"

    img = cv2.imread(img_path)

    print(temp_dict)
    for key, data in sorted(temp_dict.items()):
        
        im=Image.open(img_path)
        w= int(im.size[0])
        h= int(im.size[1])
        
        b = (data[0][0],data[0][1],data[1][0],data[1][1])
    
        x1 = b[0]
        y1 = b[1]
        x2 = b[2]
        y2 = b[3]
        xmin = min(x1,x2)
        xmax = max(x1,x2)
        ymin = min(y1,y2)
        ymax = max(y1,y2)
        b = (xmin, xmax, ymin, ymax)

        # cv2.rectangle(img,(int(xmin), int(ymin)),(int(xmax),int(ymax)),(255, 0, 0) ,2)
        # cv2.imshow("111",img)
        # cv2.waitKey(0)

        bb = convert_bbox((w,h), b)    #归一化
        # anno_list.append("%.4f" % bb[0])
        # anno_list.append("%.4f" % bb[1])
        # anno_list.append("%.4f" % bb[2])
        # anno_list.append("%.4f" % bb[3])

        final_dict[key]=["%.4f" % bb[0],"%.4f" % bb[1],"%.4f" % bb[2],"%.4f" % bb[3]]


            
    # cv2.circle(img,(int(b[0]),int(b[1])),1, (255,0,0),2)
    # cv2.imshow("111",img)
    # cv2.waitKey(0)
    print(final_dict)
    for key, dict_ind in final_dict.items():
        #参考coco.names
        if key == "cloud":
            key=0
        elif key == "house":
            key=1
        elif key == "mountain":
            key=2
        txt_outfile.write(str(key) + " " + " ".join([str(a) for a in dict_ind]) + '\n')

    #data annotation format 
    # <object-class> <x_center> <y_center> <width> <height>
  
  