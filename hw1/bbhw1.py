c__author__ = 'Bob'
import os
import matplotlib.pylab as pl
DATA_FILE = 'iris/iris.data'

def readfile(filename):
    file = open(filename)
    sepal_length_1 = []
    sepal_length_2 = []
    sepal_length_3 = []
    sepal_width_1 = []
    sepal_width_2 = []
    sepal_width_3 = []
    petal_length_1 = []
    petal_length_2 = []
    petal_length_3 = []
    petal_width_1 = []
    petal_width_2 = []
    petal_width_3 = []

    for l in file:
        a = l.strip().split(",")
        if a[4] == 'Iris-setosa':
            sepal_length_1.append(a[0])
            sepal_width_1.append(a[1])
            petal_length_1.append(a[2])
            petal_width_1.append(a[3])
        elif a[4] == 'Iris-versicolor':
            sepal_length_2.append(a[0])
            sepal_width_2.append(a[1])
            petal_length_2.append(a[2])
            petal_width_2.append(a[3])
        else:
            sepal_length_3.append(a[0])
            sepal_width_3.append(a[1])
            petal_length_3.append(a[2])
            petal_width_3.append(a[3])
    #sepal_length vs sepal_width
    pl.title('sepal_length vs sepal_width')
    pl.xlabel('sepal_length')
    pl.ylabel('sepal_width')
    pl.plot(sepal_length_1,sepal_width_1,"ro",label = "$setosa$")
    pl.plot(sepal_length_2,sepal_width_2,"gx",label = "$versicolor$")
    pl.plot(sepal_length_3,sepal_width_3,"b^",label = "$virginica$")
    pl.xlim(4.0, 8.0)
    pl.ylim(2.0, 4.5)
    pl.legend()
    pl.show()
    #sepal_length vs petal_length
    pl.title('sepal_length vs petal_length')
    pl.xlabel('sepal_length')
    pl.ylabel('petal_length')
    pl.plot(sepal_length_1,petal_length_1,"ro",label = "$setosa$")
    pl.plot(sepal_length_2,petal_length_2,"gx",label = "$versicolor$")
    pl.plot(sepal_length_3,petal_length_3,"b^",label = "$virginica$")
    pl.xlim(4, 8)
    pl.ylim(0, 10)
    pl.legend()
    pl.show()
    #sepal_length vs petal_width
    pl.title('sepal_length vs petal_width')
    pl.xlabel('sepal_length')
    pl.ylabel('petal_width')
    pl.plot(sepal_length_1,petal_width_1,"ro",label = "$setosa$")
    pl.plot(sepal_length_2,petal_width_2,"gx",label = "$versicolor$")
    pl.plot(sepal_length_3,petal_width_3,"b^",label = "$virginica$")
    pl.xlim(4, 8)
    pl.ylim(0, 3)
    pl.legend()
    pl.show()
    #sepal_width vs petal_length
    pl.title('sepal_width vs petal_length')
    pl.xlabel('sepal_width')
    pl.ylabel('petal_length')
    pl.plot(sepal_width_1,petal_length_1,"ro",label = "$setosa$")
    pl.plot(sepal_width_2,petal_length_2,"gx",label = "$versicolor$")
    pl.plot(sepal_width_3,petal_length_3,"b^",label = "$virginica$")
    pl.xlim(2, 4.5)
    pl.ylim(0, 8)
    pl.legend()
    pl.show()
    #sepal_width vs petal_width
    pl.title('sepal_width vs petal_width')
    pl.xlabel('sepal_width')
    pl.ylabel('petal_width')
    pl.plot(sepal_width_1,petal_width_1,"ro",label = "$setosa$")
    pl.plot(sepal_width_2,petal_width_2,"gx",label = "$versicolor$")
    pl.plot(sepal_width_3,petal_width_3,"b^",label = "$virginica$")
    pl.xlim(2, 4.5)
    pl.ylim(0, 3)
    pl.legend()
    pl.show()
    #petal_length vs petal_width
    pl.title('petal_length vs petal_width')
    pl.xlabel('petal_length')
    pl.ylabel('petal_width')
    pl.plot(petal_length_1,petal_width_1,"ro",label = "$setosa$")
    pl.plot(petal_length_2,petal_width_2,"gx",label = "$versicolor$")
    pl.plot(petal_length_3,petal_width_3,"b^",label = "$virginica$")
    pl.xlim(0, 8)
    pl.ylim(0, 3)
    pl.legend()
    pl.show()

def main():
    readfile(DATA_FILE);

if __name__ == '__main__':
    main()