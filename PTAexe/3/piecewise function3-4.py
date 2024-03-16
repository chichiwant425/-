import math
x=int(input())
if x>=0:
    y=math.sin(x)+2*math.sqrt(x+math.exp(4))-pow(x+1,3)
    print('函数计算结果为：y={:.2f}'.format(y))
else:
    y=math.log(-5*x)-math.fabs(x**2-8*x)/(7*x)+math.exp(1)
    print('函数计算结果为：y={:.2f}'.format(y))