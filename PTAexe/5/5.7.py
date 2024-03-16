class Pet:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def setName(self,name):
        self.__name = name
    def setAge(self,age):
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

    def __str__(self):
        return '%s is %s age!'%(self.__name,self.__age)

#  请在这里填写Pet类的定义

def main():

    # 获取数据
    pet_name = input()
    pet_age = int(input())

    # 创建一个Pet实例.
    mypet = Pet(pet_name, pet_age)

    # 显示输入的数据
    print('Here is the data that you entered: ')
    print('Pet name: ', mypet.getName())
    print('Age of pet: ', mypet.getAge())
    # 输出描述
    print(mypet)

main()
