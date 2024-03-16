class Student:
    def __init__(self,name,mscore,cscore,escore):
        self.name=name
        self.mscore=mscore
        self.cscore=cscore
        self.escore=escore

    def getSum(self):
        return self.mscore+self.cscore+self.escore
    def getBest(self):
        print(self.name,self.mscore,self.cscore,self.escore,end='')

a=input().split()
b=input().split()
c=input().split()
d=input().split()
s=list()
for i in range(len(a)):
    s.append(Student(a[i],int(b[i]),int(c[i]),int(d[i])))
s=sorted(s,key=lambda x:x.getSum(),reverse=True)
s[0].getBest()