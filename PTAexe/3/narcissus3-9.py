n=int(input())
d=[]
f=0
for a in range(10**(n-1),10**n):
    s=0
    t=a
    for b in range(1,n+1):
        c=t%10
        t=t//10
        s=s+c**n
    if a==s:
        d.append(a)
        f=f+1
for e in d[0:f-1]:
    print(e)
print(d[f-1],end='')