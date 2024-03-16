from math import pi
class Shape:
    def __init__(self,sName):
        self.sName=sName
class Rectangle(Shape):
    def __init__(self,s,w,h):
        Shape.__init__(self,s)
        self.h=h
        self.w=w
    def getArea(self):
        return self.h*self.w
class Circle(Shape):
    def __init__(self,s,r):
        Shape.__init__(self,s)
        self.r=r
    def getArea(self):
            return pi*self.r**2

s1 = Shape("shape0")
s = input()  #矩形名称
w = float(input()) #矩形宽度
h = float(input()) #矩形高度
r1 = Rectangle(s,w,h)
s = input()  #圆的名称
r = float(input()) #圆的半径
c1 = Circle(s,r)

print(s1.sName)
print("矩形%s面积: %.2f" % (r1.sName,r1.getArea()))
print("圆形%s面积: %.2f" % (c1.sName,c1.getArea()))