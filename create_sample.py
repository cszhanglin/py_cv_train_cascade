# coding:utf-8
import subprocess
import glob
import os
pos_dir = './pos/img'
vec_dir = './vec'
bg_des = './neg/bg.txt'
pos_des='./pos/pos.txt'
vector_file='./pos.vec'
width=36
height=18
# for pos_file in glob.glob(os.path.join(pos_dir, '*.jpg')):
#     filename = os.path.splitext(os.path.split(pos_file)[-1])[0]
#     vec_name = os.path.join(vec_dir, '%s.%s' % (filename, 'vec'))
#     args = []
#     args.append('%s %s' % ('-img', pos_file))
#     args.append('%s %s' % ('-vec', vec_name))
#     args.append('%s %s' % ('-bg', bg_des))
#     args.append('%s %s' % ('-num', 4))
#     args.append('%s %s' % ('-w', 36))
#     args.append('%s %s' % ('-h', 18))
#     cmd_call = 'opencv_createsamples.exe'+' '+ ' '.join(args)
#     cmd_output = subprocess.check_output(cmd_call, shell=True)
#     print cmd_call
#     print cmd_output
args=[]
args.append('-vec %s'%(vector_file))
args.append('-w %d -h %d'%(width,height))
args.append('-info %s'%(pos_des))
args.append('-num %d'%(2379))
cmd_call='opencv_createsamples.exe %s'%(' '.join(args))
print cmd_call