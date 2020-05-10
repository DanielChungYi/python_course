#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:16:03 2020

@author: daniel
"""


import cv2
import numpy as np
import os
import sys
import subprocess


path_name = "/home/daniel/test/DriveD/"
path_name_out = "/home/daniel/test/DriveD_out/"
dir = os.listdir(path_name)
#os.chdir(path_name)

for file in dir:
    img = cv2.imread(path_name+file)
    rows,cols,depth = img.shape
    
    for i in range(rows):
        for j in range(cols):
            if (pow((i-543),2)+pow((j-570),2))>260000:
                img[i,j,0]=0
                img[i,j,1]=0
                img[i,j,2]=0            
    
    cv2.imwrite(path_name_out+file, img)