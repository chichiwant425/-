n=int(input())
d=[]
f=0
for i in range(n):
    a=int(input())
    for b in range(a//2):
        if a%(b+2)==0:
           c=1
           break
        else:
            c=0
    if c==0:
        d.append('Yes')
        f+=1
    else:
        d.append('No')
        f+=1
for e in d[0:f-1]:
    print(e)
print(d[f-1],end='')