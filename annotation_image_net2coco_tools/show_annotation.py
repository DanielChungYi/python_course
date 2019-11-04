import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
import random
import csv
import argparse
import cv2

def process_command():
	parser = argparse.ArgumentParser()
	parser.add_argument('--number', '-n', type=int, required=False, help='number of image')
	return parser.parse_args()

args = process_command()
dirs = os.listdir("/shared/workshop/library_baoshan_recording/Image_Net_Person/train/Person")
os.chdir("/shared/workshop/library_baoshan_recording/Image_Net_Person/train/Person")
#image = cv2.imread("5488bf9c3bc83f7f.jpg")


for i in range(args.number):
	print("@@@@")
	filename = random.choice(dirs) #change dir name to whatever
	filename = filename.replace('txt', 'jpg')
	print(filename)
	im = Image.open(filename)
	width, height = im.size
	filename = filename.replace('jpg', 'txt')
	print(filename)
	file_txt = filename
	class_name = []
	x_min = []
	x_max = []
	y_min = []
	y_max = [] 
	width_b = []
	height_b = []


	with open(file_txt) as csvfile:
		inputcsv = csv.reader(csvfile, delimiter=',')
		for row in inputcsv:
			class_name.append(row[0])
			x_min.append(row[1])
			x_max.append(row[2])
			y_min.append(row[3])
			y_max.append(row[4])

		for i in range(len(x_min)):
			width_b.append (float(x_max[i]) -  float(x_min[i]))
			height_b.append(float(y_max[i]) -  float(y_min[i]))
			# Create a Rectangle patch
			rect = Rectangle((float(x_min[i])*width,float(y_min[i])*height),float(width_b[i])*width,float(height_b[i])*height,linewidth=2,edgecolor='b',facecolor='none')
			# Get the current reference
			ax = plt.gca()
			# Add the patch to the Axes
			ax.add_patch(rect)


	# Display the image
	plt.imshow(im)
	plt.show(ax)

   
