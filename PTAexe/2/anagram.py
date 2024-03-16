#如果一个字符串是 另一个字符串的重新排列组合，那么这两个字符串互为变位词。
#比如，”heart”与”earth”互为变位 词，”Mary”与”arMy”也互为变位词。
'''st1=input()
st2=input()
if len(st1)==len(st2):
    for i in range(len(st1)):
        if st1[i] in st2 and st2[i] in st1:
            a=0
        else:
            a=1
            break
else:
    a=1
if a==0:
    print('yes')
else:
    print('no')'''
a=input()
b=input()
if sorted(a)==sorted(b):
 print('yes')
else:
 print('no')

