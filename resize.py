# coding: utf-8
import os
from PIL import Image


curr_dir=os.path.dirname(os.path.realpath(__file__))
input_dir=os.path.join(curr_dir,'input')
out_dir=os.path.join(curr_dir,'out')
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

def get_list(line):
    line=line.strip().split(',')
    return [int(line[0]),int(line[1])]

size_list=[get_list(line) for line in open('sizes','r')]
names = os.listdir(input_dir)
for name in names:
    main_img_path=os.path.join(input_dir,name)
    main_img=Image.open(main_img_path)
    raw_name=name.split('.')[0]
    name_ext=name.split('.')[1]
    resize_dir=os.path.join(out_dir,raw_name)
    os.makedirs(resize_dir)
    for size in size_list:
        width=size[0]
        height=size[1]
        new_img_name='%s%sX%s.%s' %(raw_name,width,height,name_ext)
        new_img_path=os.path.join(resize_dir,new_img_name)
        #create new image
        main_img.resize((width,width), Image.ANTIALIAS).save(new_img_path)