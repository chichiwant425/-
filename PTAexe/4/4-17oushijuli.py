import math
def readPoint(): #从一行以,分隔的数中读取坐标，放入元组并返回
    a=input().split(",")
    for i in range(len(a)):
        if a[i]=='':a[i]=0
        else:a[i]=int(a[i])
    d = tuple(a)#元组
    return d
def distance(point): #计算point与原点的距离并返回，要math库中的函数
    s=0
    for i in range(len(point)):
        s+=point[i]**2
    a=math.sqrt(s)
    return a

n = int(input())
for i in range(n):
    p = readPoint()
    print('Point = {}, type = {}, distance = {:.3f}'.format(p,type(p),distance(p)))