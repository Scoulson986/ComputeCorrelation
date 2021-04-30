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


if __name__ == '__main__':
    workBook = xlrd.open_workbook('/Users/zhuxiaowen/Desktop/清研院/测试数据.xlsx')
    allSheetNames = workBook.sheet_names()
    sheet1Name = workBook.sheet_names()[2]
    sheet1_content2 = workBook.sheet_by_name('Sheet3')
    testX = sheet1_content2.col_values(0)
    testY = sheet1_content2.col_values(1)
    # print(ce.value)
    # arr1 = input("输入第一组数：")
    # testX = [int(n) for n in arr1.split()]
    # # print(testX)
    # arr2 = input("输入第二组数：")
    # testY = [int(n) for n in arr2.split()]
    a = int(input("输入交叉周期上限："))
    b = int(input("输入交叉周期下限："))
    for i in range(b,a+1):
        testX = shift(i, testX)
        print("交叉周期为"+repr(i)+"时，相关度r为 "+ repr(computeCorrelation(testX, testY)))
    # print(a)
    # print(b)
    # print(testY)
    # print(testX)
    # colors1 = '#DC143C'
    # area = np.pi * 2**2
    # plt.scatter(testX, testY, s=area, c=colors1, alpha=0.4, label='类别A')
    # plt.show() 