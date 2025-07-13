import sys
input = sys.stdin.readline

parent = list(input().rstrip())
pattern = list(input().rstrip())

def make_pi(pattern):
    n = len(pattern)
    pi = [0 for _ in range(n)]
    j = 0
    for i in range(1,n):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
        
    return pi


pi = make_pi(pattern)
j = 0
n = len(parent)
m = len(pattern)
res = []
for i in range(n):

    while j > 0 and parent[i] != pattern[j]:
        j = pi[j-1]
    if parent[i] == pattern[j]:
        if j == m-1:
            res.append(i-j+1)
            j = pi[j]
        else:
            j += 1

print(len(res))
print(*res)