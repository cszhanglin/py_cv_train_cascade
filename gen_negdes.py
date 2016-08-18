# coding:utf-8
import os
import glob
neg_path = './neg/'
neg_img_path = os.path.join(neg_path, 'img')
neg_description = os.path.join(neg_path, 'bg.txt')
rand_neg_path_list = []
for neg_file in glob.glob(os.path.join(neg_img_path, '*.jpg')):
    rand_neg_path_list.append(os.path.join(
        'neg','img', os.path.split(neg_file)[-1] + '\n'))

with open(neg_description, 'w') as wfile:
    wfile.writelines(rand_neg_path_list)
