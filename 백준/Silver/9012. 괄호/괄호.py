import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    cnt = 0
    s = list(input().strip())
    for i in range(len(s)):
        if s[i] == '(':
            cnt+=1
        elif s[i] == ')':
            cnt-=1
            if cnt < 0:
                break

    print("YES" if cnt == 0 else "NO")
    
