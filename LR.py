# encoding=utf-8   #encoding problem of python2
'''
Created on January 25, 2018
Logistic Regression
@author: xu
'''

from numpy import *
import matplotlib.pyplot as plt

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmoid(inX):
    return 1.0/(1 + exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)  #transfor matrix of numpy
    labelMat = mat(classLabels).transpose()

    m,n = shape(dataMatIn)
    alpha = 0.001
    maxCycles = 500
    weigths = ones((n, 1))  #initialize the ratio

    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weigths)
        error = (labelMat - h)
        weigths = weigths + alpha * dataMatrix.transpose() * error
    return weigths

def plotBestFit(wei):
    weights = wei.getA()  #transfor matrix to the array
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]

    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []

    for i in range(n):
        if int(labelMat[i] == 1):
            xcord1.append(dataArr[i, 1]); ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1]); ycord2.append(dataArr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c = 'red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c = 'green')

    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x)/weights[2]
    ax.plot(x, y)

    plt.xlabel('X1'); plt.ylabel('X1')
    plt.show()

if __name__ == "__main__":
    dataArr, labelMat = loadDataSet()
    weigths = gradAscent(dataArr, labelMat)
    plotBestFit(weigths)
    print weigths