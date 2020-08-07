# labelme-convert-yolo3-label-format
In this project, you can convert original labelme annotation json file to yolo format file.


# This is an example：

- python labelme2voc.py Root_imgs Root_imgs_convert --labels labels.txt

Ps: labels.txt means the classes numbers and classes name；Root_imgs and Root_imgs_convert represent the original labelme annotation directory and converted voc save path

- python voc2yolo.py

PS： Based on the requrements of yolo detector project ：https://github.com/ultralytics/yolov3, you should convert the yolo annotation format into this structure:

**../coco/images/train2017/000000109622.jpg  # image**

**../coco/labels/train2017/000000109622.txt  # label**

and adjsut the voc2yolo.py line15 and other values! carefully to search some detail params in this code file. you will reciveve the label dirctory in this project root directory.

may be some file structure should be adjusted,**suffle_dataset.py** will help you to suffle the probalility of train.txt and valid.txt in above convted yolo format file we just finished work.

Last, joy it!
