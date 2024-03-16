'''def xfunction(n):
    if n == 1:
        return 1;
    else:
        return n + xfunction(n - 1)
print(xfunction(4))'''

'''m=[2,1,0,5,3,5,7,4]
def naive(M,A=None):
    if A is None:
        A=set(range(len(M)))
    if len(A)==1:return(A)
    B=set(M[i] for i in A)
    #print(B)
    C=A-B
    if C:
        A.remove(C.pop())
        #print(A)
        return naive(M,A)
    return A
print(sum(list(naive(m))))'''

'''b,c=3,4
def g_func():
    a=b*c
    b=b+1
    d=a
    print(a,b,end=" ")
g_func()
print(b,c)'''

'''def he(L):
    if len(L)==0:return 0
    if len(L)==1:return L[0]
    l=he(L[0:len(L)//2])#7-5
    r=he(L[len(L)//2:len(L)])#(8+32)+(9-7)
    return l+r
L=[9,-7]#7,-5,8,32,9,-7
print(he(L))'''

#print(max(map(str,range(11)))*3)#<map object at 0x0000020EE5ACEFD0>?

'''lst=[(1,"one"),(2,"two"),(3,"three"),(4,"four")]
lst.sort(key=lambda x:x[1])
print(lst[3][1][2])#[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]'''

#print(sorted({'a':9,'b':3,'c':78}.values()),sorted([111,2,33],key=lambda x:len(str(x))))

'''x=[1,11,111]
x.sort(key=lambda x:len(str(x)),reverse=True)
print(x)'''

'''def func(x,y,z):return x+y-z
print(func(y=2,z=3,x=8))

def func(x):return x%2==1
print(list(filter(func,[10,8,9,4,3,1])))

def para_check(func):
    def wrapper(num):
        if type(num) != int:
            return 1
        elif num <= 0:
            return 2
        else:
            return func(num)
    return wrapper
def cal(rad):
    return 5 * rad
cal = para_check(cal)
print(cal("hello"))

v = 254
print(hex(v))
print(bin(v+1))
print(oct(v+1))

print(sum(list(range(1, 10, 3))))'''


def func1():
    print("11", end=" ")
def func2():
    print("22", end=" ")
def func3():
    print("33", end=" ")
funclist = [func1, func2, func3]
for func in funclist:
    func()

f = lambda p:p+5
t = lambda p:p*3
x=7
x=f(x)
x=t(x)
x=f(x)
print(x)