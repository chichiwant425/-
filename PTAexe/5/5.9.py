SLOW = 1
MEDIUM = 2
FAST = 3
class Fan:
    def __init__(self,speed=SLOW,on=False,radius=5,colo='white'):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__colo=colo
    def __str__(self):
        if self.__on:self.__on='on'
        else:self.__on='off'
        return 'speed {}\ncolor {}\nradius {}\nfan is {}'.format(self.__speed,self.__colo,self.__radius,self.__on)

    def setSpeed(self,speed):
        self.__speed=speed
    def setRadius(self,radius):
        self.__radius=radius

    def setColor(self,colo):
        self.__colo=colo
    def setOn(self,on):
        self.__on=on


def main():
    fan1 = Fan()
    print(fan1)
    print()

    fan2 = Fan()
    fan2.setSpeed(FAST)
    fan2.setRadius(10)
    fan2.setColor("blue")
    fan2.setOn(True)
    print(fan2)

main()