# coding:utf-8
import subprocess
import glob
import os

data_dir = './cascade'
vec_name = './pos.vec'
bg = './neg/bg.txt'
w = 36
h = 18
numThreads = 6
featureType = 'LBP'

args = []
args.append('-data %s' % (data_dir))
args.append('-vec %s' % (vec_name))
args.append('-bg %s' % (bg))
args.append('-w %s' % (w))
args.append('-h %s' % (h))
args.append('-numThreads %s' % (numThreads))
args.append('-featureType %s' % (featureType))
args.append('-numStages %d'%(17))
args.append('-numPos %d'%(2300))
args.append('-numNeg %d'%(4000))

cmd_call = 'opencv_traincascade.exe' + ' ' + ' '.join(args)
print(cmd_call)
# popen = subprocess.Popen(
#     cmd_call, shell=True,stdin=subprocess.PIPE, stdout=subprocess.STDOUT,stderr=subprocess.STDOUT)
