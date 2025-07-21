import sys
input = sys.stdin.readline

n,m = map(int,input().split())

d = [[] for _ in range(n)]
pos = []
for i in range(m):
    tmp = list(map(int,input().split()))
    for j in range(n):
        d[j].append(tmp[j])
    pos.append(tmp)

rpos = []

def cal_dist(key):
    dist = 0
    for i in range(m):
        for j in range(n):
            dist += abs(key[j]-pos[i][j])
    return dist

l = m // 2
for i in d:
    i.sort()
    if m % 2 == 0:
        rpos.append((i[l] + i[l-1])//2)
    else:
        rpos.append(i[l])
print(cal_dist(rpos))
print(*rpos)
