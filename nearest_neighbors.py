import numpy as np
import math

def KNN_test(X_train, Y_train, X_test, Y_test, K):
    trainSamples, numFeatures = X_train.shape
    testSamples = X_test.shape[0]

    yPred = []
    for i in range(testSamples):
        distanceArr = []
        labelArr = []
        for j in range(trainSamples):
            distance = dist(X_test[i], X_train[j], numFeatures)
            labelArr.append(Y_train[j])
            distanceArr.append(distance)
        
        npLabel = np.array(labelArr)
        npDist = np.array(distanceArr)

        sortedIndex = np.argsort(npDist)
        sortedLabel = npLabel[sortedIndex]
        sortedDist = npDist[sortedIndex]

        signSum = 0
        for k in range(K):
            signSum += sortedLabel[k]

        if signSum >= 0:
            yPred.append(1)
        else:
            yPred.append(-1)

    correct = 0
    for index in range(testSamples):
        if Y_test[index] == yPred[index]:
            correct += 1
    
    return (correct/testSamples)

def dist(p1, p2, dimens):
    fDis = 0
    for cord in range(dimens):
        fDis += pow((p1[cord] - p2[cord]), 2)
    return (math.sqrt(fDis))