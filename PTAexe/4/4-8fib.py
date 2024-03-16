def fibo(n):
    if n==1 or n==2:
        return 1
    a=1
    b=1
    i=3
    while i<=n:
        c=a+b
        a=b
        b=c
        i+=1
    return c

n=int(input())
res=fibo(n)
print(res)