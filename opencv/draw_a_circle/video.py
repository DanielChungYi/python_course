#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:26:27 2020

@author: daniel
"""

import numpy as np
import cv2
from cv2 import VideoWriter_fourcc


cap = cv2.VideoCapture('FisheyeCamera_2_out.avi')


#===========================================================
# 使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
# 建立 VideoWriter 物件，輸出影片至 output.avi
# FPS 值為 20.0，解析度為 960*720
out = cv2.VideoWriter('/home/daniel/test/output1.avi', fourcc, 10.0, (960, 720),True)
#============================================================
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)
        print(frame.shape)
        #===============================
        rows,cols,depth = frame.shape
    
        for i in range(rows):
            for j in range(cols):
                if (pow((i-360),2)+pow((j-480),2))>130000:
                    frame[i,j,0]=0
                    frame[i,j,1]=0
                    frame[i,j,2]=0      
        #===============================
        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

#=============================
