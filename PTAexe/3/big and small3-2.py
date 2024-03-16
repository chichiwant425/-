a,b,c=map(int,input().split())
if a<b:
    t=a
    a=b
    b=t
if a<c:
    t=a
    a=c
    c=t
if b<c:
    t=b
    b=c
    c=t
print('排序结果（降序）： ',end='')
print(a,b,c)