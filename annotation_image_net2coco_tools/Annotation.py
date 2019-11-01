import xml.etree.ElementTree as ET
from fractions import Fraction
import os 
import csv
import argparse

def process_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--input', '-i', type=str, required=False, help='input file name')
    parser.add_argument('--output', '-o', type=str, required=False, help='output file name')
    return parser.parse_args()

args = process_command()
dirs = os.listdir("/shared/workshop/ITRI_day-30k/Annotations")
#os.chdir("/shared/workshop/ITRI_day-30k/Annotations")
for file in dirs:
	tree = ET.parse('./Annotations/'+file)
	root = tree.getroot()

	class_name = []
	x_max = []
	x_min = []
	y_max = []
	y_min = []
	image_width = 0
	image_heigth = 0

	#extract info by tag

	for elem in tree.iter(tag='height'):
		image_heigth = float(elem.text)

	for elem in tree.iter(tag='width'):
		image_width = float(elem.text)


	for elem in tree.iter(tag='name'):
		class_name.append(elem.text)

	for elem in tree.iter(tag='xmax'):
		#class_name = []print(elem.tag) 
		#print(elem.attrib)
		#print(elem.text)
		x_max.append(elem.text)

	for elem in tree.iter(tag='xmin'):
		x_min.append(elem.text)

	for elem in tree.iter(tag='ymax'):
		y_max.append(elem.text)

	for elem in tree.iter(tag='ymin'):
		y_min.append(elem.text)

	for item in x_max:
		print(item)


	mid_x= []
	mid_y = []
	width = []
	height = []


	for i in range(len(x_min)):
		class_name[i] = class_name[i].replace('bicycle', '0')
		class_name[i] = class_name[i].replace('bus', '1')
		class_name[i] = class_name[i].replace('car', '2')
		class_name[i] = class_name[i].replace('motorbike', '3')
		class_name[i] = class_name[i].replace('person', '4') 


	def x_scale(x):
		return x / image_width
		#return float(Fraction(x,image_width))

	def y_scale(y):
		return y / image_heigth
		#return float(Fraction(y,image_height))

	for i in range(len(x_min)):
		mid_x.append(x_scale((float(x_min[i]) +  float(x_max[i])) / 2))
		mid_y.append(y_scale((float(y_min[i]) +  float(y_max[i])) / 2))
		width.append(x_scale((float(x_max[i]) -  float(x_min[i]))))
		height.append(y_scale((float(y_max[i]) -  float(y_min[i]))))
	x = file
	file_name = str(file)
	file_name = file_name.replace('xml','txt')

	with open("/home/user/daniel_ws/itri_data/labels/train/"+file_name, 'w', newline='') as csvoutFile: 
		writer = csv.writer(csvoutFile)
		writer = csv.writer(csvoutFile, delimiter=' ')
		for i in range(len(x_min)):
			writer.writerow([class_name[i],mid_x[i],mid_y[i],width[i],height[i]])
	csvoutFile.close()


'''
print('===================')
for elem in tree.iter():
    print(elem.tag) 
    #print(elem.attrib)
    print(elem.text)
'''


'''
from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('./Annotations/20161205_04-000196.xml')

items = mydoc.getElementsByTagName('x_max')

# one specific item attribute
print('Item #2 attribute:')
print(items[1].attributes['name'].value)

# all item attributes
print('\nAll attributes:')
for elem in items:
    print(elem.attributes['name'].value)

# one specific item's data
print('\nItem #2 data:')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

# all items data
print('\nAll item data:')
for elem in items:
    print(elem.firstChild.data)
'''
