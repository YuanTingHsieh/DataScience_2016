# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.lines as mline
import numpy as np
import pydot
from mpl_toolkits.mplot3d import Axes3D

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.cluster import KMeans


iris = datasets.load_iris()

X=iris.data
y=iris.target
target_names = iris.target_names

#doing PCA
pca = PCA(n_components=2)
X_r2= pca.fit(X).transform(X)

pca = PCA(n_components=3)
X_r3= pca.fit(X).transform(X)

#plot pca2
plt.figure()
for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], c=c, label=target_name)
plt.xlabel('pc1')
plt.ylabel('pc2')
plt.legend()
plt.title('PCA_2 of IRIS dataset')

#plot pca3
fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')
for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
    ax.scatter(X_r3[y == i, 0], X_r3[y == i, 1], X_r3[y==i, 2], c=c)
scatter1_proxy = mline.Line2D([0],[0], linestyle="none", c='r',marker='o')
scatter2_proxy = mline.Line2D([0],[0], linestyle="none", c='g',marker='o')
scatter3_proxy = mline.Line2D([0],[0], linestyle="none", c='b',marker='o')
ax.set_xlabel('pc1')
ax.set_ylabel('pc2')
ax.set_zlabel('pc3')
ax.legend([scatter1_proxy, scatter2_proxy,scatter3_proxy], ['setosa','versicolor','virginica'], numpoints = 1)
plt.title('PCA_3 of IRIS dataset')

#doing DecisionTreeClassify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

dot_data=StringIO()
tree.export_graphviz(clf,out_file=dot_data,feature_names=iris.feature_names)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")

#doing K-means
num_k=np.arange(1,9,1)
for kk in num_k:
  est=KMeans(n_clusters=kk)
  est.fit(X)
  newlabel=est.labels_

  fig=plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=newlabel.astype(np.float))
  ax.set_xlabel('Petal width')
  ax.set_ylabel('Sepal length')
  ax.set_zlabel('Petal length')
  plt.title(str(kk)+'-means clustering')

plt.show()
