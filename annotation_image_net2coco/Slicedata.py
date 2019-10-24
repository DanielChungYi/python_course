import os
import argparse
import subprocess

def process_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    #parser.add_argument('--input', '-i', type=str, required=True, help='Text for program')
    #parser.add_argument('--output', '-o', type=str, required=False, help='Text for program')
    return parser.parse_args()

args = process_command()

dirs = os.listdir("/home/user/daniel_ws/itri_data/images/train/")
f_train= open("/home/user/daniel_ws/itri_data/list/coco_5cls_train.txt","a+")
f_val = open("/home/user/daniel_ws/itri_data/list/coco_5cls_val.txt","a+")
f_test = open("/home/user/daniel_ws/itri_data/list/coco_5cls_test.txt","a+")
count = int(0);
val_List = []

for file in dirs:
   count += 1
   # method 1 List
   #x = list(file)

   # method 2 Str   
   x = file
   x = x.replace('txt','jpg')
   #x = x.replace('.txt','')
   print(x)
   
   if count < 1500:
       f_test.write("/home/user/daniel_ws/itri_data/images/train/"+file+'\n')
       val_List.append(x)
       #subprocess.run([ 'mkdir', 'aaa'])
       #subprocess.call('cp '+file+' ../test_10/', shell=True)
       #subprocess.call(['cp','-r','./'+args.input+'/'+file, filename], shell = False)
       #subprocess.call(['rm','-r','./'+args.input+'/'+file], shell = False)


   elif count < 6000 and count >=1500:
       f_val.write("/home/user/daniel_ws/itri_data/images/train/"+file+'\n')
     
   else:
       f_train.write("/home/user/daniel_ws/itri_data/images/train/"+file+'\n')  

print(count)
