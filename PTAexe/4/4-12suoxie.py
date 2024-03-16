def acronym(phrase):
    a=phrase.split()
    b=''
    for i in range(len(a)):
        b+=str(a[i][0])
    return b.upper()

phrase=input()
print(acronym(phrase))