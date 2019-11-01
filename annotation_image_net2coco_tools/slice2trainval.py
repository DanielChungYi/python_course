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

dirs = os.listdir("//home/user/test/images/"+args.input)
f_train= open("coco_5cls_train.txt","a+")
f_val = open("coco_5cls_val.txt","a+")
f_test = open("coco_5cls_test.txt","a+")
count = int(0);
val_List = []
filename = '/home/user/daniel_ws/yolov3/data/samples/'
for file in dirs:
   count += 1
   # method 1 List
   #x = list(file)

   # method 2 Str   
   x = file
   x = x.replace('.jpg','')
   x = x.replace('.txt','')
   print(x)
   
   if count < 300:
       f_test.write("/home/user/test/images/train5class/"+file+'\n')
       val_List.append(x)
       #subprocess.run([ 'mkdir', 'aaa'])
       #subprocess.call('cp '+file+' ../test_10/', shell=True)
       subprocess.call(['cp','-r','./'+args.input+'/'+file, filename], shell = False)
       #subprocess.call(['rm','-r','./'+args.input+'/'+file], shell = False)

'''
   elif count >= 1000:
       f_train.write("/home/user/test/images/train5class/"+file+'\n')
'''    

print(count)
