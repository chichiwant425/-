class Shape:
    def length(self):
        pass
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def length(self):
        if self.a>0 and self.b>0 and self.c>0:return self.a+self.b+self.c
        else:return 0
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def length(self):
        if self.a>0 and self.b>0:return (self.a+self.b)*2
        else:return 0
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def length(self):
        if self.r>0:return 3.14*self.r*2
        else:return 0
lines = []
while True:
    try:
        i=list(map(int,input().split()))
        if len(i)==1:
            c=Circle(i[0])
            print('{:.2f}'.format(c.length()))
        elif len(i)==2:
            c=Rectangle(i[0],i[1])
            print('{:.2f}'.format(c.length()))
        else:
            c=Triangle(i[0],i[1],i[2])
            print('{:.2f}'.format(c.length()))
    except:break

