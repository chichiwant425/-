def isflower(n):
    s=0
    t=n
    for i in range(1,4):
        c = t % 10
        t = t // 10
        s=s+c**3
    if n==s:
        return True
    else:
        return False

n = eval(input())
if isflower(n)==True:
    print('Yes')
else:
    print('No')