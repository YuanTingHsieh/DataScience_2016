# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import itertools as itool

f = open('./iris/iris.data','r')

datas=[]
for l in  f.readlines():
    data = l.strip().split(',')    
    datas.append(data[:])

datas=np.array(datas)
datas=datas[datas[:,4].argsort()]

#np.savetxt('./data_fuck',datas,delimiter=",",fmt="%s")

data_class=np.array(datas[:,4])
datas=np.array(datas[:,0:4],dtype='float')

#keys is the classes of data
keys,indices = np.unique(data_class,return_index=True)

types=['sepal_length','sepal_width','petal_length','petal_width']
types_num=[0,1,2,3]
typescom=[]
numcom=[]
for gg in itool.combinations(types,2):
  typescom.append(gg)
for gg in itool.combinations(types_num,2):
  numcom.append(gg)

colors=['r','b','k']
markers=['o','x','d']
locs=[1,4,4,7,7,4]

plt.rcParams["figure.figsize"]=[20,10]
fig,axarr = plt.subplots(2,3)
#mgr=plt.get_current_fig_manager()
#mgr.window.setGeometry(50,100,640,545)
for x in range(2):
  for y in range(3):
    for i in range(3):
      axarr[x,y].scatter(datas[ 0+50*i:50+50*i , numcom[x*3+y][0] ],datas[0+50*i:50+50*i, numcom[x*3+y][1] ],label=keys[i],color=colors[i],marker=markers[i])
      axarr[x,y].set_title(typescom[x*3+y][0]+' vs '+typescom[x*3+y][1])
      axarr[x,y].set_xlabel(typescom[x*3+y][0])
      axarr[x,y].set_ylabel(typescom[x*3+y][1])
      axarr[x,y].legend(scatterpoints=1,loc=locs[x*3+y],fontsize='small')
    #plt.scatter(datas[50:99,0],datas[50:99,1],lebel=keys[1],color='b',marker='x')
    #plt.scatter(datas[100:149,0],datas[100:149,1],label=keys[2],color='k',marker='d')
plt.show()


f.close()
