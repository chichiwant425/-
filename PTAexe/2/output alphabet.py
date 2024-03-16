#随机输入一个字符串，把最左边的10个不重复的英文字母（不区分大小写）挑选出来。
#如没有10个英文字母，显示信息“not found”
a=input()
b=''
for i in range(len(a)):
    if a[i].isalpha()==True and a[i].upper() not in b.upper():
        b=b+a[i]
if len(b)>=10:
    for i in range(10):
        print(b[i],end='')
else:
    print('not found',end='')
