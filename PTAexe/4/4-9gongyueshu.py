def fun(a,b):
    if a<b:
        x=a
        y=b
    else:
        x=b
        y=a
    for i in range(2,x):
        if a%i==0 and b%i==0:
            m=i
        else:m=1
    for i in range(y,a*b+1):
        if i%a==0 and i%b==0:
            n=i
            break
    return m,n

m,n=map(int,input().split())
s=fun(m,n)
print("最大公约数为%d，最小公倍数为%d。"%(s[0],s[1]))
