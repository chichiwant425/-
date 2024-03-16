def f(n):
    if n==1 or n==2:
        return 1
    a=f(n-1)+f(n-2)
    return a

n=int(input())
print(f(n))