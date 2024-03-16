def sum(n):
    i=1
    s=0
    while i<=n:
        s+=i
        i+=1
    return s

n=int(input())
print("1+2+...+{0}={1}".format(n,sum(n)) )