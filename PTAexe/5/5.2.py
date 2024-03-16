class Book:
    def __init__(self,sName,sNo,fPrice):
        self.sName=sName
        self.sNo=sNo
        self.fPrice=round(fPrice,2)
    def __del__(self):
        print('Book destroyed-',end='')
        print(self.sName,self.sNo,self.fPrice,sep=',',end='')

sName = input()  #输入书名
sNo = input() #输入书号
fPrice = float(input())   #输入单价
b = Book(sName,sNo,fPrice)
b = None   #触发b对象的__del__方法的执行