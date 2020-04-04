#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import h5py
import os
from PIL import Image

f=h5py.File("nyu_depth_v2_labeled.mat")
depths=f["depths"]
depths=np.array(depths)

path_converted='./nyu_depths/'
if not os.path.isdir(path_converted):
    os.makedirs(path_converted)

max = depths.max()
print depths.shape
print depths.max()
print depths.min()

depths = depths / max * 255
depths = depths.transpose((0,2,1))

print depths.max()
print depths.min()

for i in range(len(depths)):
    # labels_number.append(labels[i])
    # labels_0=np.array(labels_number[i])
    # print labels_0.shape
    # print type(labels_0)
    print str(i) + '.png'
    depths_img= Image.fromarray(np.uint8(depths[i]))
    depths_img = depths_img.transpose(Image.FLIP_LEFT_RIGHT)
    #depths_img = depths_img.transpose((1,0,2));
    # depths_img = depths_img.rotate(270)
    iconpath=path_converted+str(i)+'.png'
    depths_img.save(iconpath, 'PNG', optimize=True)
