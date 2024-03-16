a=input().split(",")
for i in range(len(a)):
    if a[i]=='':a[i]=0
    else:a[i]=int(a[i])
d=tuple(a)
print(d)