import math
def funcos(eps,x):
    s=0
    i=0
    c=1
    while math.fabs(c)>eps:
        b=1
        if i!=0:
            for a in range(1,i+1):
                b*=a
        c=((-1)**(i/2))*(x**i)/b
        if math.fabs(c)>eps:
            s+=c
        i+=2
    return s

eps,x=input().split()
eps,x=float(eps),float(x)
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))