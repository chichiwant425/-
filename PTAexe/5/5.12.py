from operator import itemgetter
T = int(input())
while T>0:
    T-=1
    n=int(input())
    a=[]
    for i in range(0,n+1):
        s1={'No': i,'Grade':0,'j1':0,'j2':0}
        a.append(s1)
    for i in range(n*(n-1)//2):
        s = input().split()
        if s[2] > s[3]:
            a[int (s[0])]['Grade'] += 3
            a[int (s[0])]['j1'] += int(s[2])- int(s[3])
            a[int (s[1])]['j1'] += int(s[3]) - int(s[2])
            a[int (s[0])]['j2'] += int(s[2])
            a[int (s[1])]['j2'] += int(s[3])
        elif s[2] < s[3]:
            a[int (s[0])]['j1'] += int(s[2]) - int(s[3])
            a[int (s[1])]['j1'] += int(s[3]) - int(s[2])
            a[int (s[0])]['Grade'] +=3
            a[int (s[0])]['j2'] += int(s[2])
            a[int (s[1])]['j2'] += int(s[3])
        else:
            a[int(s[0])]['j1'] += int(s[2]) - int(s[3])
            a[int(s[1])]['j1'] += int(s[3]) - int(s[2])
            a[int(s[0])]['Grade'] += 1
            a[int(s[1])]['Grade'] += 1
            a[int(s[0])]['j2'] += int(s[2])
            a[int(s[1])]['j2'] += int(s[3])
    a = sorted(a,key = itemgetter('Grade','j1','j2'),reverse=True)
    print(a)
    b=[]
    #for i in range(n):
        #for j in a[i]['No']:
            #b.append(j)
    #print(b)







