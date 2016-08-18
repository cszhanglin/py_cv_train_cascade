# coding:utf-8
import cv2
import os
import glob
import numpy as np
import random as rd
import re

pic_path = 'F:/PlateProj/PlateRecData'
neg_path = './neg/'
pos_path = './pos/'
pos_img_path = os.path.join(pos_path, 'img')
neg_img_path = os.path.join(neg_path, 'img')

neg_description = os.path.join(neg_path, 'bg.txt')

def overlap(roi_1,roi_2):
    colInt =  min(roi_1[0]+roi_1[2],roi_2[0]+roi_2[2]) - max(roi_1[0], roi_2[0])  
    rowInt =  min(roi_1[1]+roi_1[3],roi_2[1]+roi_2[3]) - max(roi_1[1],roi_2[1])
    return colInt>0 and rowInt>0

def gen_neg_one_pic(pic, width=136, height=36,exclude_roi=((0,0),(0,0))):
    rows, cols = pic.shape[0:2]
    roi_x_b, roi_y_b = rd.randint(
        0, cols - width - 1), rd.randint(0, rows - height - 1)
    return (roi_x_b,roi_y_b,width,height)


for imgfile in glob.glob(os.path.join(pic_path, '*.jpg')):
    img = cv2.imread(imgfile)
    filename = os.path.splitext(os.path.split(imgfile)[-1])[0]
    pos_file = glob.glob(os.path.join(pos_img_path, filename+'*'))
    if pos_file:
        pos_file = pos_file[0]
        pos_filename=os.path.splitext(os.path.split(pos_file)[-1])[0]
        mode=re.compile(r'_(\d+)_(\d+)_(\d+)_(\d+)_(\d+)')
        match=mode.findall(pos_filename)
        match=map(int,list(match[0]))
        exclude_roi=(match[1],match[2],match[3],match[4])
        ext = os.path.splitext(os.path.split(imgfile)[-1])[-1]
        for i in range(100):
            rand_neg_roi = gen_neg_one_pic(img)
            if overlap(exclude_roi,rand_neg_roi):
                print 'overlapped with positive region'
                continue
            rand_neg=img[rand_neg_roi[1]:rand_neg_roi[1]+rand_neg_roi[3],rand_neg_roi[0]:rand_neg_roi[0]+rand_neg_roi[2],:]

            rand_neg_path = os.path.abspath(os.path.join(
                neg_img_path, '%s_%d' % (filename, i) + ext))
            cv2.imwrite(rand_neg_path, rand_neg)

    # ext = os.path.splitext(os.path.split(imgfile)[-1])[-1]
    # for i in range(100):
    #     rand_neg = gen_neg_one_pic(img)
    #     rand_neg_path = os.path.abspath(os.path.join(
    #         neg_img_path, '%s_%d' % (filename, i) + ext))
    #     cv2.imwrite(rand_neg_path, rand_neg)
