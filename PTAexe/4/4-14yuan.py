import math
def getCircleArea(r):#r代表整数半径
    r=float(r)
    s=math.pi*(r**2)
    return s
def get_rList(n):#n代表在函数中输入n个值放入列表。
    a=list()
    for i in range(n):
        b=int(input())
        a.append(b)
    return a

n = int(input())
rList = get_rList(n)
for e in rList:
    print('{:10.3f}'.format(getCircleArea(e)))
print(type(rList))