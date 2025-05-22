import sys
input = sys.stdin.readline

S = ['K','O','R','E','A']
s1 = list(input().strip())

idx = 0
res = 0
for i in range(len(s1)):
    if s1[i] == S[idx]:
        res += 1
        idx = (idx+1) % 5
print(res)