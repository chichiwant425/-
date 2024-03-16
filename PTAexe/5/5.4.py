class Stock:
    'Stock Information Class'
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.__sCode=sCode
        self.__sName=sName
        self.__priceYesterday=priceYesterday
        self.__priceToday=priceToday
    def getCode(self):
        return self.__sCode
    def getName(self):
        return self.__sName
    def getPriceYesterday(self):
        return self.__priceYesterday
    def setPriceYesterday(self,priceYesterday):
        self.__priceYesterday=priceYesterday
    def getPriceToday(self):
        return self.__priceToday
    def setPriceToday(self,priceToday):
        self.__priceToday=priceToday
    def getChangePercent(self):
        return (self.__priceToday-self.__priceYesterday)/self.__priceYesterday


sCode = input() #输入代码
sName = input() #输入名称
priceYesterday = float(input())  #输入昨日价格
priceToday = float(input())  #输入今日价格
s = Stock(sCode,sName,priceYesterday,priceToday)
print("代码:",s.getCode())
print("名称:",s.getName())
print("昨日价格:%.2f\n今天价格:%.2f" % (s.getPriceYesterday(),s.getPriceToday()))
s.setPriceYesterday(50.25)
print("修正昨日价格为:%.2f" % 50.25)
print("价格变化百分比:%.2f%%" % (s.getChangePercent()*100))
print(Stock.__doc__)