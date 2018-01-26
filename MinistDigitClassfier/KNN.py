# encoding=utf-8   #encoding problem of python2
'''
Created on January 26, 2018
kNN:k Nearest Neighbors
@author: xu
'''
from numpy import *
import operator
from os import listdir
import time

#transfer digit picture to the vector
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i +j] = int(lineStr[j])

    return returnVect

'''
Using the Euclidean distance formula to get the distance of two vector
inX:vector to compare to existing dataSet(1*n)
dataSet:training dataset(N*M)
labels:data set labels(1*M)
k:number of neighbors to use for compare(should be the an odd bunber)
'''
def clsssify0(inX, dataSet, labels, k):
    dataSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSize, 1)) - dataSet  #calculate the distance between \
                                                  # inX to every example of dataSet
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis = 1)
    distance = sqDistance**0.5
    sortedDistIndicies = distance.argsort()  #indice of distance ascending
    classCount = {}

    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')  #get contents of files
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))

    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])  #get digit

        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % (fileNameStr))

    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)

    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % (fileNameStr))
        classifierResult = clsssify0(vectorUnderTest, trainingMat, hwLabels, 3)

        print "the classfier came back with:%d, the real answer is:%d" % (classifierResult, classNumStr)
        if(classifierResult != classNumStr):
            errorCount += 1.0

    print("\nthe total number of error is:%d" % errorCount)
    print("\nthe total error rate is:%f" % (errorCount/float(mTest)))

if __name__ == "__main__":
    startTime = time.time()
    handwritingClassTest()
    print("spending %.2fs!" % (time.time() - startTime))