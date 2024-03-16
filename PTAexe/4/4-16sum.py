def sum(m,n):
    i=m
    s=0
    while i<=n:
        s+=i
        i+=1
    return s

m=int(input())
n=int(input())
print(sum(m,n))