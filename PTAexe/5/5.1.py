class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def getBMI(self):
        return self.weight/(self.height**2)
    def getStatus(self):
        if self.weight/(self.height**2)<18:
            return '超轻'
        elif self.weight/(self.height**2)<25:
            return '标准'
        elif self.weight/(self.height**2)<27:
            return '超重'
        else:return '肥胖'

sName = input()  #输入姓名
iAge = int(input()) #输入年龄
fHeight = eval(input())  #输入身高，预期为浮点数，单位米
fWeight = eval(input())  #输入体重，预期为浮点数，单位千克
bmi=BMI(sName,iAge,fHeight,fWeight) #实例化BMI类
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())