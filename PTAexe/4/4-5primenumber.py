import math
def isPrime(num):
    try:
        num=int(num)
    except Exception:
        return False
    else:
        a=int(math.sqrt(num))+1
        for i in range(2,a+1):
            if num%i==0:
                return False
        return True

num=input()
if isPrime(num):
    print('Yes')
else:
    print('No')