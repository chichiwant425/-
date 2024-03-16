n=int(input())
a=1
b=2
for i in range(n):
    if b<=n:
        t=b
        b=b+a
        a=t
        i+=1
    else:
        break
print(b)