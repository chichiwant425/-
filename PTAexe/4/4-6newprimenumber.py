import math
def isPrime(num):
    if num==1:
        return False
    a=int(math.sqrt(num))+1
    for i in range(2,a):
        if num%i==0:
            return False
    return True

def reverseNumber(num):
    a=str(num)
    t=num
    s=0
    for i in range(len(a)-1,-1,-1):     #len(a)到0的递减数列
        b=t%10
        t=t//10
        s+=b*(10**i)
    return s

N = int(input())
for n in range(1,N+1):
    if isPrime(n) and reverseNumber(n) == n:
        print(n)