from math import sqrt
def prime(p):
    a=int(sqrt(p))+1
    i=2
    b=0
    if p == 1:
        b = 1
    elif p == 2:
        b = 0
    else:
        while i<=a:
            if p%i==0:
                b=1
                break
            i+=1
    if b==0:
        return True
    else:
        return False

def PrimeSum(m,n):
    s=0
    for i in range(m,n+1):
        if prime(i):
            s+=i
    return s

m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))