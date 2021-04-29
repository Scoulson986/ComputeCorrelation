# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from astropy.units import Ybarn
import math
import xlrd
import xlwt
import tkinter as tk

on_hit = False
def calculate():
    global on_hit
    if on_hit == False:
        on_hit = True

        destination=d.get()
        workBook = xlrd.open_workbook(destination)
        sheetX = sX.get()
        sheetY = sY.get()
        sheetX_content = workBook.sheet_by_name(sheetX)
        sheetY_content = workBook.sheet_by_name(sheetY)
        n=int(Xc2.get())-int(Xc1.get())+1 #column
        m=int(Xr2.get())-int(Xr1.get())+1 #row
        horX=int(Xr1.get())-1
        verX=int(Xc1.get())-1
        A = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                A[i][j] = sheetX_content.cell_value(i+horX,j+verX)
                A[i][j] = float(A[i][j])

        n1 = int(Yc2.get())-int(Yc1.get())+1
        m1 = int(Yr2.get())-int(Yr1.get())+1
        horY=int(Yr1.get())-1
        verY=int(Yc1.get())-1
        B = [[0]*n1 for i in range(m1)]
        for i in range(m1):
            for j in range(n1):
                B[i][j] = sheetY_content.cell_value(i+horY,j+verY)
                B[i][j] = float(B[i][j])
        # print(A)
        # print(B)
        a=int(up.get())
        b=int(down.get())
        bigfuc(A,B,a,b)
    else:
        on_hit = False

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
        if varX == varY == 0:
            SSR = 1
            varX = varY = 1

    SST = math.sqrt(varX * varY)
    return SSR / SST


def shift(key, array):
    return array[-key:]+array[:-key]


def bigfuc(X, Y, a, b):
    lenX = len(X)
    widthX = len(X[0])
    lenY = len(Y)
    widthY = len(Y[0])
    X = np.array(X)
    Y = np.array(Y)
    for i in range(widthX):
        for j in range(widthY):
            print("X组第"+repr(i+1)+"列Y组第"+repr(j+1)+"列")
            fuc(X[:, i], Y[:, j], a, b, lenX, lenY)


def fuc(testX, testY, a, b, lenX, lenY):
    X1 = [int(n) for n in range(lenX-1)]
    Y1 = [int(n) for n in range(lenY-1)]
    X1 = testX.tolist()
    Y1 = testY.tolist()
    # num=list(range(b,a+1))
    r = list(range(b, a+1))
    for i in range(b, a+1):
        X2 = shift(i, X1)
        if X2 == Y1:
            r[i] = 1
        else:
            r[i] = computeCorrelation(X2, Y1)
        print("交叉周期为"+repr(i)+"时，相关度r为 " + repr(r[i]))
    # return zip(num,r)

# UI configuration
window = tk.Tk()
window.title('相关度分析')
window.geometry('600x200')
l = tk.Label(window, text="输入excel文件位置:",)
l.pack()
l.place(x=0, y=0, anchor='nw')
l2 = tk.Label(window, text="输入X组数据的工作表名称:",)
l2.pack()
l2.place(x=0, y=30, anchor='nw')
l3 = tk.Label(window, text="输入Y组数据的工作表名称:",)
l3.pack()
l3.place(x=300, y=30, anchor='nw')
l4 = tk.Label(window, text="X组数据从第",)
l4.pack()
l4.place(x=0, y=60, anchor='nw')
l5 = tk.Label(window, text="行",)
l5.pack()
l5.place(x=120, y=60, anchor='nw')
l6 = tk.Label(window, text="到",)
l6.pack()
l6.place(x=140, y=60, anchor='nw')
l7 = tk.Label(window, text="行",)
l7.pack()
l7.place(x=200, y=60, anchor='nw')
l8 = tk.Label(window, text="X组数据从第",)
l8.pack()
l8.place(x=0, y=90, anchor='nw')
l9 = tk.Label(window, text="列",)
l9.pack()
l9.place(x=120, y=90, anchor='nw')
l10 = tk.Label(window, text="到",)
l10.pack()
l10.place(x=140, y=90, anchor='nw')
l11 = tk.Label(window, text="列",)
l11.pack()
l11.place(x=200, y=90, anchor='nw')
l12 = tk.Label(window, text="Y组数据从第",)
l12.pack()
l12.place(x=300, y=60, anchor='nw')
l13 = tk.Label(window, text="行",)
l13.pack()
l13.place(x=420, y=60, anchor='nw')
l14 = tk.Label(window, text="到",)
l14.pack()
l14.place(x=440, y=60, anchor='nw')
l15 = tk.Label(window, text="行",)
l15.pack()
l15.place(x=500, y=60, anchor='nw')
l16 = tk.Label(window, text="Y组数据从第",)
l16.pack()
l16.place(x=300, y=90, anchor='nw')
l17 = tk.Label(window, text="列",)
l17.pack()
l17.place(x=420, y=90, anchor='nw')
l18 = tk.Label(window, text="到",)
l18.pack()
l18.place(x=440, y=90, anchor='nw')
l19 = tk.Label(window, text="列",)
l19.pack()
l19.place(x=500, y=90, anchor='nw')
l21 = tk.Label(window, text="输入交叉周期上限",)
l21.pack()
l21.place(x=0, y=120, anchor='nw')
l22 = tk.Label(window, text="输入交叉周期下限",)
l22.pack()
l22.place(x=300, y=120, anchor='nw')

d = tk.Entry(window,)
d.pack()
d.place(x=130, y=0, anchor='nw')
sX = tk.Entry(window, width=10)
sX.pack()
sX.place(x=180, y=30, anchor='nw')
sY = tk.Entry(window, width=10)
sY.pack()
sY.place(x=480, y=30, anchor='nw')
Xr1 = tk.Entry(window, width=3)
Xr1.pack()
Xr1.place(x=80, y=60, anchor='nw')
Xr2 = tk.Entry(window, width=3)
Xr2.pack()
Xr2.place(x=160, y=60, anchor='nw')
Xc1 = tk.Entry(window, width=3)
Xc1.pack()
Xc1.place(x=80, y=90, anchor='nw')
Xc2 = tk.Entry(window, width=3)
Xc2.pack()
Xc2.place(x=160, y=90, anchor='nw')
Yr1 = tk.Entry(window, width=3)
Yr1.pack()
Yr1.place(x=380, y=60, anchor='nw')
Yr2 = tk.Entry(window, width=3)
Yr2.pack()
Yr2.place(x=460, y=60, anchor='nw')
Yc1 = tk.Entry(window, width=3)
Yc1.pack()
Yc1.place(x=380, y=90, anchor='nw')
Yc2 = tk.Entry(window, width=3)
Yc2.pack()
Yc2.place(x=460, y=90, anchor='nw')
up = tk.Entry(window, width=10)
up.pack()
up.place(x=120, y=120, anchor='nw')
down = tk.Entry(window, width=10)
down.pack()
down.place(x=420, y=120, anchor='nw')

s = tk.Button(window, text='计算', width=15, height=2, command=calculate)
s.pack()
s.place(x=300, y=150, anchor='nw')


if __name__ == '__main__':
    window.mainloop()

