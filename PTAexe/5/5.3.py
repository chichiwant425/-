from math import sqrt
class Root:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def getDiscriminant(self):
        return self.b**2-4*self.a*self.c
    def getRoot1(self):
        return (-self.b+sqrt(self.b**2-4*self.a*self.c))/(2*self.a)
    def getRoot2(self):
        return (-self.b-sqrt(self.b**2-4*self.a*self.c))/(2*self.a)

a=float(input()) #请输入二次项系数
b=float(input()) #请输入一次项系数
c=float(input()) #请输入常数项系数

root=Root(a,b,c)
if root.getDiscriminant()>0:
    print("{:.2f}".format(root.getRoot1()))
    print("{:.2f}".format(root.getRoot2()))
elif root.getDiscriminant()==0:
    print("{:.2f}".format(root.getRoot1()))
else:
    print("No Root!")
