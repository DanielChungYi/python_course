import csv
import os
import argparse


def process_command():
	parser = argparse.ArgumentParser()
	parser.add_argument('--foo', help='foo help')
	parser.add_argument('--input', '-i', type=str, required=False, help='Text for program')
	parser.add_argument('--output', '-o', type=str, required=False, help='Text for program')
	return parser.parse_args()

args = process_command()
dirs = os.listdir("/home/user/daniel_ws/library_data/labels/train/")
os.chdir("/home/user/daniel_ws/library_data/labels/train/")
f= open("/home/user/daniel_ws/library_data/list/label_list.txt","a+")
for file in dirs:
    class_name = []
    x_min = []
    x_max = []
    y_min = []
    y_max = []  
    with open(file) as csvfile:
   	 inputcsv = csv.reader(csvfile, delimiter=',')
   	 for row in inputcsv:
   	 	class_name.append(row[0])
   	 	x_min.append(row[1])
   	 	x_max.append(row[2])
   	 	y_min.append(row[3])
   	 	y_max.append(row[4])

    mid_x= []
    mid_y = []
    width = []
    height = []

    #replace
    for i in range(len(x_min)):
   	 class_name[i] = class_name[i].replace('Person', '0')


    #print(len(inputcsv))
    for i in range(len(x_min)):
   	 print(float(x_min[i]) +  float(x_max[i]))
   	 mid_x.append((float(x_min[i]) +  float(x_max[i])) / 2)
   	 mid_y.append((float(y_min[i]) +  float(y_max[i])) / 2)
   	 width.append (float(x_max[i]) -  float(x_min[i]))
   	 height.append(float(y_max[i]) -  float(y_min[i]))

    csvfile.close()
    with open("/home/user/daniel_ws/library_data/labels/train2/"+file, 'w', newline='') as csvoutFile:
   	 writer = csv.writer(csvoutFile)
   	 writer = csv.writer(csvoutFile, delimiter=' ')
   	 for i in range(len(x_min)):
     		 writer.writerow([class_name[i],mid_x[i],mid_y[i],width[i],height[i]])
   	 csvoutFile.close()
    f.write("/home/user/daniel_ws/library_data/labels/train/"+file+'\n')
f.close()

