'''print('{0},{2},{1}'.format('a','b','c'))
print(pow(-3, 2), round(18.67, 1), round(18.67, -1))
print("hello" 'world')
print(sum((1,3,5,7,9))/len((1,3,5,7,9)))'''

'''s="test.txt"
print(s[-5:5])
x=9
x%=5
print(x)
lst=[3,4,5,6,5,4,3]
lst.remove(3)
print(lst)
text="four score and 7 years"
lenwords={s:len(s) for s in text.split()}
#print(text.split())
print(lenwords["score"])
lst=[23,56,8,900,24]
print(lst[::-1])
def main():
    s = [12,-4,32,-36,12,6,-6]
    s_max, s_sum = 0, 0
    #print(s)
    for i in range(len(s)):
        s_sum += s[i]
        if s_sum >= s_max:
            s_max = s_sum
        elif s_sum < 0:
            s_sum = 0
    print(s_max)
main()
x=set(range(2,5))
print(x)
while True:
   print("我爱学python")
x=5
y=6
if(x>y):
    print(x)

a=[3,5,7,11,13,16,21,24,28,32,36,40,46]
x = int(input())
found = -1
left = 0                      #第一个元素下标
right = len(a)-1              #最后一个元素下标
while left<right:
    mid = (left + right) // 2
    if a[mid] > x:
        right = mid - 1
    elif a[mid] < x:
        left = mid + 1
    else:                     # a[mid]==x
        found = mid
        break
print(found)
x=2;y=2.0
if(x==y):
  print('相等')
else:
  print('不相等')

while True: 
    pass
num=int(input())
a=num-1
while a>1:
  if num % a == 0:
     print("不是素数")
     break
  a=a-1
else:
  print("是素数")

s=0
for i in range(5):
   s=s+i
print("s={}".format(s))

s=0
a,b=1,2
if a>0:
    s=s+1
elif b>0:
    s=s+1
print(s)

x = 5
y = 3
z = 8
print(not (x < y or z > x) and y < z)

t = int(input())
if t > 32:
    print("Cool")
elif t > 86:
    print("Hot")
else:
    print("Freezing")

score = 70
if score < 70:
    if score > 60:
        print("OK")
    else:
        print("Effort")
else:
    if score < 70:
        print("Good")
    else:
        print("Excellent")

day=4
x=1
while day>0:
    x=(x+1)*2
    day-=1
print(x)

number = 25
isPrime = True
for i in range(2, number):
  if number % i == 0:
    isPrime = False
    break
print("i is", i, "isPrime is", isPrime)

cat =['狮子','猎豹','虎猫','花豹','孟加拉虎','美洲豹','雪豹']
for s in cat:
    if '豹' in s:
        print(s,end=' ')
        continue
print(a)'''

decimal = eval(input("Enter an integer: "))
hexString = ""
value = decimal
while value != 0:
    single = value % 16
    if single == 15:
        hexString = "F" + hexString
    elif single == 14:
        hexString = "E" + hexString
    elif single == 13:
        hexString = "D" + hexString
    elif single == 12:
        hexString = "C" + hexString
    elif single == 11:
        hexString = "B" + hexString
    elif single == 10:
        hexString = "A" + hexString
    else:
        hexString = str(single)+ hexString
    value =value//16
print(str(decimal) + "'s hex representation is " + hexString)