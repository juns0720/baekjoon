import sys
input = sys.stdin.readline

s1 = list(input().strip())
n = len(s1)
def make_pi(s):
    n = len(s)
    pi = [0 for _ in range(n)]
    j = 0
    cnt = 0
    for i in range(1,n):
        while j > 0 and (s[i] != s[j]):
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            cnt = max(cnt, j)
            pi[i] = j
    return cnt
res = 0
for i in range(n):
    cnt = make_pi(s1[i:])
    res = max(res,cnt)
print(res)