import math
b,c=map(int,input().split())
if b**2-4*c>=0:
    x1=(-b+math.sqrt(b**2-4*c))/2
    x2=(-b-math.sqrt(b**2-4*c))/2
    print('x1=',x1)
    print('x2=',x2,end='')
else:
    print('此方程无实数解')