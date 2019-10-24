import os
import argparse
import pandas as pd
import numpy as np
import operator
#fout.close() 
dirs = os.listdir("/home/user/daniel_ws/yolov3/result")
os.chdir("/home/user/daniel_ws/yolov3/result")
best = {}
#for (key, value) in wordFreqDic.items() :
#        print(key , " :: ", value )
print(best)

for file in dirs:
    #print(file)
    df = pd.read_csv(file)
    df_ = df.as_matrix()
    x = np.array(df_)
    for i in x[8]:
        z = i.split("    ",15)
        #print(z[11])
        best.update({file : float(z[11])})
#print(best)

best_lr = max(best.items(), key=operator.itemgetter(1))[0]
print(best_lr)


#open(file)  或是 pd.read_csv(file) 讀進來的每一列都為string
#用 split把每一列當中的每個 column 分開
