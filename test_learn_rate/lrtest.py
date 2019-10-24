import sys 
import subprocess
import argparse
from pathlib import Path
import os
import numpy as np
from subprocess import call

#dir = os.listdir("/home/chris/III_ITRI_intensity_local_12_v2_submaps")
os.chdir("/home/user/daniel_ws/yolov3/")
path = os.getcwd()
if os.path.exists(path):
	print("oooooooooooooo")
if not os.path.exists(path):
    print("xxxxxxxxxxxxxx")
'''
a = 0.001
b = str(a)
subprocess.call(['python3', 'train.py','--data','data/coco_5cls.data','--cfg','cfg/yolov3-5cls.cfg','--batch-size','4','--epochs','2','--accumulate','8','--lr',b,'--name',b])
'''
#cmd = "python3 train.py --data data/coco_5cls.data --cfg cfg/yolov3-5cls.cfg --batch-size 4 --epochs 100 --accumulate 8 --lr 0.01"
#subprocess.call(cmd)
#subprocess.run(cmd)
count = 0
def frange(start, stop=None, step=None):

    if stop == None:
        stop = start + 0.0
        start = 0.0

    if step == None:
        step = 1.0

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield ("%g" % start) # return float number
        start = start + step

print ("Printing float range")
floatList = frange(0.001, 0.01, 0.0001)
for num in floatList:
    print (num)
    lr = str(num)
    subprocess.call(['python3', 'train.py','--data','data/coco_5cls.data','--cfg','cfg/yolov3-5cls.cfg','--batch-size','4','--epochs','10','--accumulate','8','--lr',lr,'--name',lr])
    count += 1
print(count)

