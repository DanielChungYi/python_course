import os
import argparse
import subprocess

def process_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--input', '-i', type=str, required=True, help='Text for program')
    #parser.add_argument('--output', '-o', type=str, required=False, help='Text for program')
    return parser.parse_args()

args = process_command()

dirs = os.listdir("/home/user/test/images/"+args.input)
f= open("coco_5cls_train.txt","a+")
f2 = open("coco_5cls_val.txt","a+")
count = int(0);
val_List = []
for file in dirs:
   count += 1
   # method 1 List
   #x = list(file)

   # method 2 Str   
   x = file
   x = x.replace('.jpg','')
   x = x.replace('.txt','')
   print(x)
   
   if count < 10:
       f2.write("/home/user/test/images/val5class/"+file+'\n')
       val_List.append(x)
       subprocess.run([ 'cp', file ./test_10])
'''
   elif count >= 10:
       for item in val_List:
           
           val_List[item]
       f.write("/home/user/test/images/train5class/"+file+'\n')
       val_List.
'''
print(count)
