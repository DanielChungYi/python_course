import sys 
import subprocess
import argparse
from pathlib import Path
import os

dir = os.listdir("/home/chris/III_ITRI_intensity_local_12_v2_submaps")
os.chdir("/home/chris/Downloads/pcl-master/build")
for file in dir:
    cmd = file
    print(file)
    ply = file.replace("pcd","ply")
    subprocess.call("pcl_pcd2ply /home/chris/III_ITRI_intensity_local_12_v2_submaps/"+file+" "+"/home/chris/daniel_ws/itri_ply/"+ply)
