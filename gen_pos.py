# coding:utf-8
import cv2
import os
import glob
pos_path = './pos/img'
pos_description = './pos/pos.txt'

output_list = []
for pos_file in glob.glob(os.path.join(pos_path, '*.png')):
    img = cv2.imread(pos_file)
    out_str = '%s 1 %d %d %d %d \n' % (os.path.join('img',os.path.split(pos_file)[-1]), 0, 0, img.shape[1], img.shape[0])
    output_list.append(out_str)
with open(pos_description,'w') as wfile:
	wfile.writelines(output_list)
