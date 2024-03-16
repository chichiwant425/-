a=1
b=1
for i in range(12):
    print(a,end=' ')
    c=b
    b=b+a
    a=c
    i+=1
print()
