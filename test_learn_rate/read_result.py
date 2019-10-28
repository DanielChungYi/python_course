import os
import argparse
import pandas as pd
import numpy as np
import operator
import re
import matplotlib.pyplot as plt
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
    x = df.as_matrix()
    #x = np.array(df_)
    #print(x[8])
    z = re.split(" +",str(x[8]))
    #print(z)
    best.update({file : float(z[11])})
#print(best)

best_lr = max(best.items(), key=operator.itemgetter(1))[0]
print(best_lr)
x_plot = np.array([])
y_plot = np.array([])

for key, value in best.items():
    x_plot_temp = key.split('_')
    x_plot_temp = x_plot_temp[1].rsplit('.',1)
    x_plot = np.append(x_plot , float(x_plot_temp[0]))
    y_plot = np.append(y_plot , float(value))
    print(key)
    print(value)

print(x_plot)
print(y_plot)


fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(x_plot, y_plot)
fig.suptitle('random lr vs mAP (10 epoch)')
plt.autoscale(enable=True, axis='both', tight=None)
plt.xlabel('learning rate')
plt.ylabel('mAP')
plt.show()
