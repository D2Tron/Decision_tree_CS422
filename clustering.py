import numpy as np
import random
from scipy.spatial import distance

def K_Means(X, K, mu):
    if (K <= 0):
        print("K value must be 1 or greater! Enter valid input")
    else:
        numSamples, dimensions = X.shape
        
        if (mu == []):
            mu = np.zeros((K, dimensions))
            for i in range(K):
                muRand = random.randint(0, numSamples-1)
                mu[i] = X[muRand]

        muRows, muCols = mu.shape

        clusters = [[] for i in range(K)]
        clusterIndex = 0
        
        for i in range(numSamples):
            minDist = 99999
            for j in range(K):
                dist = distance.euclidean(X[i], mu[j])
                if (dist < minDist):
                    minDist = dist
                    clusterIndex = j
            clusters[clusterIndex].extend(X[i])

        newMu = np.zeros((muRows, muCols))

        for j in range(K):
            mean = sum(clusters[j])/len(clusters[j])
            newMu[j] = mean

        comparison = mu == newMu
        checkEqual = comparison.all()

        if checkEqual == False:
            K_Means(X, K, newMu)
        
        return newMu