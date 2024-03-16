class Student:
    count=0
    def __init__(self,code,name):
        self.code=code
        self.name=name
        Student.count+=1
    def __del__(self):
        Student.count-=1

n = int(input())  #输入学生数量，数量大于1
s = []
for i in range(n):
    s.append(Student("Code"+str(i),"Name"+str(i)))
del s[0]  #删除一个学生，导致count减1
print("学生数量:",Student.count)
for x in s:
    print(x.code,x.name)