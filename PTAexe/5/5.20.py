import math
import decimal
class Rect(object):
    def __init__(self,l,h,z):
        self.l = l
        self.h = h
        self.z = z
    def length(self):
        return 2*(self.l+self.h)
    def area(self):
        return self.l*self.h
class Cubic(Rect):
    def __init__(self,l,h,z):
        super(Cubic,self).__init__(l,h,z)
    def area(self):
        return 2*(self.l*self.h) + 2*(self.h*self.z) + 2* (self.l*self.z)
    def tj(self):
        return super(Cubic,self).area() * self.z
    def show(self):
        print('{} {}'.format(decimal.Decimal(self.area()).quantize(decimal.Decimal('0.00')),decimal.Decimal(self.tj()).quantize(decimal.Decimal('0.00'))),end=' ')
class Pyramid(Rect):
    def __init__(self,l,h,z):
        super(Pyramid,self).__init__(l,h,z)
    def area(self):
        return self.l*self.h + self.h*math.sqrt(self.z**2+(self.l/2)**2) + math.sqrt(self.z**2+(self.h/2)**2)*self.l
    def tj(self):
        return super(Pyramid,self).area() * self.z / 3
    def show(self):
        print('{} {}'.format(decimal.Decimal(self.area()).quantize(decimal.Decimal('0.00')),decimal.Decimal(self.tj()).quantize(decimal.Decimal('0.00'))))
if __name__ == '__main__':
    while True:
        try:
            lst = input().split(' ')
            a = float(lst[0])
            b = float(lst[1])
            c = float(lst[2])
            if a <= 0 or b <= 0 or c <= 0:
                print('0.00 0.00 0.00 0.00')
            else:
                m = Cubic(a, b, c)
                m.show()
                n = Pyramid(a, b, c)
                n.show()
        except:
            break
