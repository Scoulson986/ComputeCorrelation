import numpy as np
from astropy.units import Ybarn
import math

def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0
    varX = 0
    varY = 0
    for i in range(0, len(X)):
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        SSR += (diffXXBar * diffYYBar)
        varX += diffXXBar**2
        varY += diffYYBar**2

    SST = math.sqrt(varX * varY)
    return SSR / SST


arr1 = input("输入第一组数：")
testX = [int(n) for n in arr1.split()]
# print(testX)
arr2 = input("输入第二组数：")
testY = [int(n) for n in arr2.split()]
# print(testY)
print("相关度r:", computeCorrelation(testX, testY))
