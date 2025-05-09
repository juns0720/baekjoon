import sys
input = sys.stdin.readline

m,n = map(int,input().split())

univ = []
for _ in range(m):
    tmp = []
    for a,b in enumerate(list(map(int,input().split()))):
        tmp.append([a,b])
    tmp = sorted(tmp, key = lambda x: x[1])
    for i in range(1,n):
        if tmp[i][1] == tmp[i-1][1]:
            tmp[i][0] = tmp[i-1][0]
    univ.append(' '.join([str(i[0]) for i in tmp]))
res = 0
for i in range(m):
    for j in range(i+1,m):
        if univ[i] == univ[j]:
            res += 1
print(res)
