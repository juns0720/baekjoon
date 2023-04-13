import sys
input = sys.stdin.readline

s = list(input().strip())
mid = len(s)//2
f = True
for i in range(mid):
    if s[i] == s[-1-i]:
        f = True
    else:
        f = False
        print(0)
        break
if f == True:
    print(1)