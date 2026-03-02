import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().split())))
visited = [0 for _ in range(n)]
S = [-1 for _ in range(n*2)]


def recursion(s, depth):
    if depth == n:
        print(*S)
        exit()
    for i in range(n):
        if visited[i]:
            continue

        e = s + arr[i] + 1
        if e > 2*n-1:
            break

        if S[e] == -1 and S[s] == -1:
            S[e], S[s] = arr[i], arr[i]
            visited[i] = 1
            ns = s
            while ns < 2*n-1 and S[ns+1] != -1 :
                ns+= 1
            recursion(ns+1, depth + 1)
            S[e], S[s] = -1, -1
            visited[i] = 0
        

recursion(0, 0)
print(-1)