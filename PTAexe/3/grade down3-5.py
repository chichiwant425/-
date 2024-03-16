a,b=map(int,input().split())
if b>a:
    t=a
    a=b
    b=t
print('降序值：',end='')
print(a,b,sep=',')