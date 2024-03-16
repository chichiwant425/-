'''class Count:
   def __init__(self, count = 0):
     self.__count = count

c1 = Count(2)
c2 = Count(2)
print(id(c1) == id(c2), end = " ")

s1 = "Good"
s2 = "Good"
print(id(s1) == id(s2))

class A:
    def __init__(self, i =1):
        self.i = i

class B(A):
    def __init__(self, j = 2):
        super().__init__()
        self.j = j

def main():
    b = B()
    print(b.i, b.j)

#程序执行
main()

class Account:
    def __init__(self,id):
        self.id=id
        id=1688

acc=Account(100)
print(acc.id)

from math import *
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
    def getPerimeter(self):
        return 2 * self.radius * pi
    def getArea(self):
        return self.radius * self.radius * pi
    def setRadius(self, radius):
        self.radius = radius

a = Circle(10)
print("{:.1f},{:.2f}".format(a.getPerimeter(),a.getArea()))

class Fun:
    def __init__(self):
        print("Fun.__init__()")
    def test(self):
        print("Fun")
class InheritFun(Fun):
    def __init__(self):
        print("InheritedFun.__init__()")
        super().__init__()
    def test(self):
        super().test()
        print("InheritedFun")
a = InheritFun()
a.test()

class Person(object):
    def __init__(self,name,gender,birth):
       self.name = name
       self.gender = gender
       self.birth = birth
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1')
print(xiaoming.name)

class account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
acc1 = account('1234', 100)
acc1.deposit(500)
acc1.withdraw(200)
print(acc1.balance)

def conflict(board, nextx):
    nexty = len(board)
    for i in range(nexty):
        if abs(board[i] - nextx) in (0, nexty - i):
            return True
    return False
def queens(num=8, board=[6, 1]):
    for pos in range(num):
        if not conflict(board, pos):
            if len(board) == num - 1:
                yield [pos]
            else:
                for result in queens(num, board + [pos]):
                    yield [pos] + result
print(len(list(queens(8))))

class Fun:
    def __init__(self):
        print("Fun.__init__()")
    def test(self):
        print("Fun")
class InheritFun(Fun):
    def __init__(self):
        print("InheritedFun.__init__()")
        super().__init__()
    def test(self):
        super().test()
        print("InheritedFun")
a = InheritFun()
a.test()

from math import *
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
    def getPerimeter(self):
        return 2 * self.radius * pi
    def getArea(self):
        return self.radius * self.radius * pi
    def setRadius(self, radius):
        self.radius = radius
a = Circle(10)
print("{:.1f},{:.2f}".format(a.getPerimeter(),a.getArea()))'''

class Person(object):        #类的定义，object固定写法
    def __init__(self,name,age,tag):     #类的构造函数，即类的初始化
        self.Name = name
        self.Age = age
        self.Tag = tag
    def introduce(self):  # 类的方法
        message = '''----------Information---------
        Name is :%s
        Age is:%s
        Tag is:%s
        ''' %  (self.Name, self.Age, self.Tag)
        print(message)
    def modif_tag(self, newtag):  # 类的方法
        self.Tag=newtag  # 修改初始化的参数

person1 = Person("罗翔","50","教师")
person1.introduce()
person2 = Person("张三","23","法外狂徒")     #把一个Person类实例化，即为实例
person2.modif_tag("守法公民")   #实例调用类的方法
person2.introduce()