import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
scores = [list(map(int,input().split())) for _ in range(n)]

scores.sort(key = lambda x: (-x[1]))

res = 0
for i in range(k):
    res += scores[i][0]
scores = sorted(scores[k:], key = lambda x: -x[0])

for i in range(m):
    res += scores[i][0]

print(res)