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
        if varX==varY==0:
            SSR=1
            varX=varY=1

    SST = math.sqrt(varX * varY)
    return SSR / SST


def shift(key, array):
    return array[-key:]+array[:-key]


def bigfuc(X,Y,a,b):
    lenX=len(X)
    widthX=len(X[0])
    lenY=len(Y)
    widthY=len(Y[0])
    X=np.array(X)
    Y=np.array(Y)
    for i in range(widthX):
        for j in range(widthY):
            print("X组第"+repr(i+1)+"列Y组第"+repr(j+1)+"列")
            fuc(X[:,i],Y[:,j],a,b,lenX,lenY)
    



def fuc(testX,testY,a,b,lenX,lenY):
    X1 = [int(n) for n in range(lenX-1)]
    Y1 = [int(n) for n in range(lenY-1)]
    X1 = testX.tolist()
    Y1 = testY.tolist()
    # num=list(range(b,a+1))
    r=list(range(b,a+1))
    for i in range(b,a+1):
        X2 = shift(i, X1)
        if X2==Y1:
            r[i]=1
        else:
            r[i]=computeCorrelation(X2, Y1)
        print("交叉周期为"+repr(i)+"时，相关度r为 "+ repr(r[i]))
    # return zip(num,r)



if __name__ == '__main__':

    n=int(input("输入X组数据行数："))
    m=int(input("输入X组数据列数："))
    A=[[0]*n for i in range(m)]
    print("输入X组数据:")
    for i in range(m):
        A[i]=input().split(" ")
        for j in range(n):
            A[i][j] = int(A[i][j])

    n1=int(input("输入Y组数据行数："))
    m1=int(input("输入Y组数据列数："))
    B=[[0]*n1 for i in range(m1)]
    print("输入Y组数据:")
    for i in range(m1):
        B[i]=input().split(" ")
        for j in range(n1):
            B[i][j] = int(B[i][j])
    # print(A)
    # print(B)
    a = int(input("输入交叉周期上限："))
    b = int(input("输入交叉周期下限："))
    bigfuc(A,B,a,b)
    

