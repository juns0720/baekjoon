import sys
input = sys.stdin.readline
N = int(input())

cnt = N
for i in range(N):
    s = list(input().strip())
    
    for j in range(0,len(s)-1):
        if s[j] == s[j+1]:
            pass
        elif s[j] in s[j+1:]:
            cnt-=1
            break
print(cnt)


