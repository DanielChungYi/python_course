import os
import argparse
#dirs = os.listdir("/home/user/daniel_ws/yolov3/data/coco/labels/train2014")

def process_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--input', '-i', type=str, required=True, help='Text for program')
    parser.add_argument('--output', '-o', type=str, required=True, help='Text for program')
    return parser.parse_args()

if __name__ == '__main__':
    args = process_command()
    #print("dir"+args.input)
    #print("dir"+args.output)
    #print("/home/user/test/labels/"+args.output+"/"+file+".txt")
    dirs = os.listdir("/home/user/test/labels/"+args.input)
	#f= open("test_py.txt","w+")
	#fout = open("/home/user/test/labels/dir_output.txt", "wt")
    os.chdir("/home/user/test/labels/"+args.input)
	#os.chdir("/home/user/daniel_ws/yolov3/data/coco/labels/train2014")
    for file in dirs:
        #print(file)
        fin = open(file, "rt")
        data = fin.read()
        data = data.replace('Bat', '0')
        data = data.replace('Bear', '1')
        data = data.replace('Bee', '2')
        data = data.replace('Ice_cream', '3')
        data = data.replace('Boot', '4')
        data = data.replace(',', ' ')
        fin.close()
        fout = open("/home/user/test/labels/"+args.output+"/"+file+".txt", "wt")
        fout.write(data)
        fout.close() 
