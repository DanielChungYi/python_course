import os
import argparse


def process_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--input', '-i', type=str, required=True, help='Text for program')
    #parser.add_argument('--output', '-o', type=str, required=False, help='Text for program')
    return parser.parse_args()

args = process_command()

dirs = os.listdir("/home/user/test/images/"+args.input)
f= open("coco_5cls_train.txt","a+")
for file in dirs:
   print(file)
   f.write("/home/user/test/images/train5class/"+file+'\n')
