import numpy as np

def DT_train_binary(X, Y, max_depth):
    numSamples, numFeatures = X.shape
    print(X, Y)
    posLabels = 0
    negLabels = 0
    for i in Y:
        if i == 1:
            posLabels += 1
        else:
            negLabels += 1

    entropyWhole = entropyCalc(numSamples, posLabels, negLabels)
    print(entropyWhole)

    maxGain = 0
    maxGainfeat = 0
    for j in range(0, numFeatures):
        #print("Feature: ", j)
        noCount = 0
        yesCount = 0
        noCountYes = 0
        noCountNo = 0
        yesCountYes = 0
        yesCountNo = 0

        for i in range(0, numSamples):
            if X[i, j] == 0:
                noCount += 1
                if Y[i] == 0:
                    noCountNo += 1
                else:
                    noCountYes += 1
            else:
                yesCount += 1
                if Y[i] == 0:
                    yesCountNo += 1
                else:
                    yesCountYes += 1

        #print("No: ", noCount, " Yes: ", yesCount)
        #print("No/No: ", noCountNo, " No/Yes: ", noCountYes)
        #print("Yes/No: ", yesCountNo, " Yes/Yes: ", yesCountYes)

        noRatio = noCount/(noCount+yesCount)
        yesRatio = yesCount/(noCount+yesCount)
        
        noEntropy = entropyCalc(noCount, noCountYes, noCountNo)
        yesEntropy = entropyCalc(yesCount, yesCountYes, yesCountNo)
        
        infoGain = infoGainCalc(entropyWhole, noEntropy, yesEntropy, noRatio, yesRatio)
        
        if (infoGain > maxGain):
            maxGain = infoGain
            maxGainfeat = 

def entropyCalc(denom, pos, neg):
    if denom == 0:
        return 0
    
    posProb = pos/denom
    negProb = neg/denom

    posEntProd, negEntProd = 0, 0
    if (pos != 0):
        posEntProd = posProb * np.log2(posProb)
    if (neg != 0):
        negEntProd = negProb * np.log2(negProb)
        
    return ( -1 * (posEntProd + negEntProd) )

def infoGainCalc(entrpy, noEntrpy, yesEntrpy, noProbs, yesProbs):
    return (entrpy - (noEntrpy*noProbs + yesEntrpy*yesProbs))

