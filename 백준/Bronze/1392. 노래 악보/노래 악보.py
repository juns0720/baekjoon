import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
check = []
for i in range(1,N+1):
    tmp = int(input())
    for j in range(tmp):
        check.append(i)
for i in range(Q):
    idx = int(input())
    print(check[idx])
