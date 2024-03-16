n =int(input())
fact = 1
i = 1
while i <= n:
    fact =fact*i
    i=i+1
print('{}!={}'.format(n,fact))

'''for i in range(1,6):
   for j in range(i):
       print('*', end='')
   print()

from math import sqrt
x=0
while True:
    a=x+100
    b=x+268
    a=sqrt(a)
    b=sqrt(b)
    if a%1==0 and b%1==0:
       print(x)
       break
    x+=1

def binarySearch(s,v):
    begin,end = 0, len(s)-1
    while begin <= end:
        mid =(begin+end)//2+1
        if s[mid] == v:
            print("Found:%d" % mid)
            break
        elif v > s[mid]:
            begin =mid
        else:
            end = mid - 1
    else: print("Not found")
a = [1,3, 12, 45, 66, 89, 123, 154, 768, 9921]
binarySearch(a,89)'

contacts = [{"name": "zhang san", "mobile": 13900001234}, {"name": "li si", "mobile": 13600001234}]
name = input()
isFound=False
for contact in contacts:
    if contact["name"]==name:
        isFound = True
        print(contact["mobile"])
        break
if isFound != True:
    print("用户不存在")'''