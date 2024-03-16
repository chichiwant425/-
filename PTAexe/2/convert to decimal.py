#输入一个整数和进制，转换成十进制输出
a,b=input().split(',')
sum=0
for i in range(len(a)):
    sum+=int(a[i])*int(b)**(len(a)-i-1)
print(sum)