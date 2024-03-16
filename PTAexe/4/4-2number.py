def CountDigit(number,digit ):
    a=str(number)
    s=0
    for i in range(len(a)):
        if str(digit)==a[i]:
            s+=1
    return s

number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)