import sys
input = sys.stdin.readline

s = list(input().strip())



res = 0
for i in range(len(s)):
    if s[i] == 'O':
        res += 2**(i) 
print(res% (10**9+7))