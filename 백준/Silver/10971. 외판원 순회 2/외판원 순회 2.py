import sys
input = sys.stdin.readline

n = int(input())
city = [list(map(int,input().split())) for _ in range(n)]
search = []

def check(c1,cost,cnt,n,first):
    visited[c1] = True
    if cnt == n and city[c1][first] != 0:
        cost+=city[c1][first]
        search.append(cost)
        visited[c1] = False
        return
    for c2 in range(n):
        if c1 != c2 and visited[c2] != True and city[c1][c2] != 0:
            cost+=city[c1][c2]
            check(c2,cost,cnt+1,n,first)
            visited[c2] = False
            cost-=city[c1][c2]

for i in range(n):
    visited = [False for i in range(n)]
    check(i,0,1,n,i)
print(min(search))
            