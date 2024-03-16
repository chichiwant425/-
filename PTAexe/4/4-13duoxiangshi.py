def polyvalue(lst,x):
    s=0
    for i in range(len(lst)):
        s+=lst[i]*(x**i)
    return s

lst=eval(input())
y=float(input())
print("{:.1f}".format(polyvalue(lst,y)))