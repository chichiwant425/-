a,b=map(int,input().split())
x=set(range(a,b))
n=0
for i in x:
    if i%3==0 and i%5==0 and i%7==0:
        n+=1
print(n)
