'''
Created on January 28, 2018
Decision Tree Source Code based on the dataSet of watermelon
@author: xu
'''

from math import log
import operator
import treePlotter

def createDataSet():
    dataSet = [[0, 0, 0, 0, 0, 0, 'yes'],
               [1, 0, 1, 0, 0, 0, 'yes'],
               [1, 0, 0, 0, 0, 0, 'yes'],
               [0, 0, 1, 0, 0, 0, 'yes'],
               [2, 0, 0, 0, 0, 0, 'yes'],
               [0, 1, 0, 0, 1, 1, 'yes'],
               [1, 1, 0, 1, 1, 1, 'yes'],
               [1, 1, 0, 0, 1, 0, 'yes'],
               [1, 1, 1, 1, 1, 0, 'no'],
               [0, 2, 2, 0, 2, 1, 'no'],
               [2, 2, 2, 2, 2, 0, 'no'],
               [2, 0, 0, 2, 2, 1, 'no'],
               [0, 1, 0, 1, 0, 0, 'no'],
               [2, 1, 1, 1, 0, 0, 'no'],
               [1, 1, 0, 0, 1, 1, 'no'],
               [2, 0, 0, 2, 2, 0, 'no'],
               [0, 0, 1, 1, 1, 0, 'no']]
    labels = ['color', 'root', 'stroke', 'texture', 'navel', 'touch']
    return dataSet, labels

# calcualte the entropy
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for festVec in dataSet:
        currentLabel = festVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    #print labelCounts
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)

    return retDataSet

# get information gain
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1

    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        #print "featList :%s"%featList
        uniqueVals = set(featList)
        #print "uniqueVals :%s"%uniqueVals
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            #print "subDataSet :%s"%subDataSet
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if len(dataSet[0]) == 2:   #if dataSet has only one attribute
        return majorityCnt(classList)
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatlabel = labels[bestFeat]

    myTree = {bestFeatlabel : {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    print featValues
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatlabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree

if __name__ == "__main__":
    myDat, labels = createDataSet()
    myTree = createTree(myDat, labels)
    print myTree
    treePlotter.createPlot(myTree)
