import math
a=input('Please enter the length of the three sides of the triangle：').split(' ')
h=(int(a[0])+int(a[1])+int(a[2]))/2
s=math.sqrt(h*(h-int(a[0]))*(h-int(a[1]))*(h-int(a[2])))
print('area=',s)