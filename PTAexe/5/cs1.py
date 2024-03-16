'''class Pet:
    def __init__(self,name):
        self.__sName = name
    def getName(self):
        return self.__sName
class Rabbit(Pet):
    def __init__(self, name):
        Pet.__init__(self,name)

    def speak(self):
        print(f"Hello from rabbit {self.getName()}.")

    def eat(self,iWeight):
        print(f"Rabbit {self.getName()} ate {iWeight} gram's food.")
class Cat(Pet):
    def __init__(self,name):
        Pet.__init__(self,name)
    def eat(self,iWeight):
        print(f"Cat {self.getName()} ate {iWeight} gram's food.")
class DragonLi(Cat):
    def __init__(self,name):
        Cat.__init__(self, name)
    def speak(self):
        print(f"Hello from dragonli cat {self.getName()}.")
class Persian(Cat):
    def __init__(self,name):
        Cat.__init__(self,name)
    def speak(self):
        print(f"Hello from persian cat {self.getName()}.")

print("-------------Rabbit Charlie--------------")
r = Rabbit("Charlie")
r.eat(100)
r.speak()

print("-------------Cat Lucy--------------")
c1 = DragonLi("Lucy")
c1.eat(200)
c1.speak()

print("-------------Cat Eddie--------------")
c2 = Persian("Eddie")
c2.eat(100)
c2.speak()'''


'''class Vector3D:
    def __init__(self,x,y,z):
        self.x,self.y,self.z=x,y,z
    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x,self.y,self.z)
    def __add__(self, v):
        return Vector3D(self.x + v.x,self.y + v.y,self.z + v.z)
    def __sub__(self,v):
        return Vector3D(self.x-v.x,self.y-v.y,self.z-v.z)
    def length(self):
        return (self.x**2+self.y**2+self.z**2)**(1/2)

v1 = Vector3D(1,2,3)
v2 = Vector3D(4,5,6)
v3 = v1 + v2
v4 = v2 - v1
print("v1 =",v1)
print("Length of v1 = %.4f" % v1.length())
print(f"{v1}+{v2}={v3}")
print(f"{v2}-{v1}={v4}")'''

'''class Rect:
    def __init__(self, tl, br):
        self.tl, self.br = tl, br

    def width(self):
        t = self.br.x -self.tl.x
        return t if t > 0 else -t

    def height(self):
        t =self.br.y -self.tl.y
        return t if t > 0 else -t

    def area(self):
        return self.width() *self.height()

    def topRight(self):
        return Point(self.br.x,self.tl.y)

    def bottomLeft(self):
        return Point(self.tl.x,self.br.y)

    def diagonalLength(self):
        return self.br-self.tl
class Point:
    def __init__(self,x,y):
        self.x, self.y = x, y

    def __sub__(self,p):
        return ((self.x-p.x)**2+(self.y-p.y)**2)**(1/2)

    def __str__(self):
        return str((self.x, self.y))

rt = Rect(Point(1,6),Point(7,8))

print("Vertices of rectangle rt:")
print(f"{rt.tl}-----------------------------{rt.topRight()}")
print(f"{rt.bottomLeft()}-----------------------------{rt.br}")
print("Size information of rectangle rt:")
print(f"width - {rt.width()},height - {rt.height()}")
print(f"area - {rt.area()},diagonal length - " \
    f"{rt.diagonalLength():.4f}")'''

class Force:
    def __init__(self,x,y):
        self.fx,self.fy = x, y

    def show(self):
        return "(%f,%f)"%(self.fx,self.fy)
    __repr__ = show

    def __lt__(self,force2):
        return self.fx*self.fx + self.fy*self.fy < force2.fx*force2.fx+ force2.fy*force2.fy

fList = [Force(1,2), Force(0,2),Force(3,4),Force(2,1)]

ff = fList.copy()
ff.sort()
print(ff)
ft = sorted(fList,key =lambda x:x.fx**2+x.fy**2)
print(ft)


