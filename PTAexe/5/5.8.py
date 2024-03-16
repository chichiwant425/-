class CountedSet(set):
    adict={}
    def __init__(self):
        set.__init__(self)
    def getCount(self,x):
        return CountedSet.adict.get(x)
    def add(self,v):
        set.add(self,v)
        if CountedSet.adict.get(v,False):
            CountedSet.adict[v]+=1
        else:CountedSet.adict[v]=1



s = CountedSet()
while True:      #用q表示输入结束
    v = input()  #输入一个字符串
    if (v!="q"):
        s.add(v)
    else:
        break
print(s)
#将集合转换成列表，排序递增输出
t = sorted(list(s))
print("元素值 次数")
for x in t:
    print(x,"-",s.getCount(x))

print("集合内元素个数:",len(s))