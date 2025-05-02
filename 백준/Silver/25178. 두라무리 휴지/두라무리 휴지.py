import sys
input = sys.stdin.readline

n = int(input())
tmp = ['a','e','i','o','u']

s1 = list(input().strip())
s2 = list(input().strip())

res1 = []
res2 = []

if sorted(s1) != sorted(s2) or not (s1[0] == s2[0] and s1[-1] == s2[-1]):
    print("NO")
    exit()

for i in range(1,n-1):
    if s1[i] not in tmp:
        res1.append(s1[i])
    if s2[i] not in tmp:
        res2.append(s2[i])
if len(res1) != len(res2) or ''.join(res1) != ''.join(res2):
    print("NO")
    exit()
    
print("YES")