import sys
import itertools
input = sys.stdin.readline

while True:
    s = input().strip()
    a = []
    if s == '*':
        break
    for i in str(s):
        a.append(i)
    if len(a) == 1:
        ans = True
    y = 1
    while y < len(a):
        ans = True
        cnt = 0
        set1 = set()
        for i in range(0,len(a)-y):
           t = a[i]+a[y+i]
           set1.add(t)
           cnt+=1
        if len(set1) != cnt:
            ans = False
        if ans == False:
            break
        y+=1
    if ans == True:
        print(s+' is surprising.')
    elif ans == False:
        print(s+' is NOT surprising.')
        