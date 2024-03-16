def is_palindrom(s):
    a=len(str(s))
    for i in range(a):
        if str(s)[i]!=str(s)[a-1-i]:
            return False
    return True

s=input()
print(is_palindrom(s))