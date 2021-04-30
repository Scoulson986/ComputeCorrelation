import numpy as np
import matplotlib.pyplot as plt
from astropy.units import Ybarn
import math
import xlrd
import xlwt


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


def shift(key, array):
    return array[-key:]+array[:-key]

def fuc(testX,testY,a,b):
    testX = [int(n) for n in arr1.split()]
    testY = [int(n) for n in arr2.split()]
    num=list(range(b,a+1))
    r=list(range(b,a+1))
    for i in range(b,a+1):
        X1 = shift(i, testX)
        num[i]=i
        if X1==testY:
            r[i]=1
        else:
            r[i]=computeCorrelation(X1, testY)
        print("交叉周期为"+repr(i)+"时，相关度r为 "+ repr(r[i]))
        print(X1)
    return zip(num,r)



if __name__ == '__main__':
    arr1 = input("输入第一组数：")
    arr2 = input("输入第二组数：")
    a = int(input("输入交叉周期上限："))
    b = int(input("输入交叉周期下限："))
    s=list(fuc(arr1,arr2,a,b))
    print(s)
    

