'''a,b = input().split(',')
b=int(b)
c=int('a',b)
print(c)'''

'''x=int(input())
if x==0:
    result=0
else:
    result=1/x
print('f({0:.1f}) = {1:.1f}'.format(x,result))'''

'''f=lambda x,y=8,z=8:x+y+z
print(f(8))'''

'''import math
def factors(x):
    y=int(math.sqrt(x))
    for i in range(2,y+1):
       if (x %i ==0):
            print(i,end=' ');
            factors(x//i)
            break
       else:
           print(x,end=' ')
    return
factors(18)


def f(a,b,c):
    print(a*b/c)
f(c=5,a=6,b=10)'''

'''x=3
def f():
    #global x
    x=5
f()
print(x)'''

'''f=lambda x:3
print(f(4))'''

#print(list(map(lambda x:len(x),['a','12','ab123'])))

'''def main():
    print("The answer is", magic(5))
def magic(num):
    answer = num + 2 * 10
    return answer
main()'''

'''def pass_it(x, y):
    z = x + ", " + y
    return(z)
name2 = "Tony"
name1 = "Gaddis"
fullname = pass_it(name1, name2)
print(fullname)'''

'''def pass_it(x, y):
    z = y**x
    return(z)
num1 = 3
num2 = 4
answer = pass_it(num1, num2)
print(answer)'''

def pass_it(x, y):
    z = x*y
    result = get_result(z)
    return(result)
def get_result(number):
    z = number + 2
    return(z)
num1 = 3
num2 = 4
answer = pass_it(num1, num2)
print(answer)
