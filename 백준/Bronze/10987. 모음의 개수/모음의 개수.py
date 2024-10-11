import sys
input = sys.stdin.readline

s = input().strip()

cnt = 0
for i in s:
    if i in ['a','e','i','o','u']:
        cnt+=1
print(cnt)