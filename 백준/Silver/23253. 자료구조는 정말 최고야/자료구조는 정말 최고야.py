import sys
input = sys.stdin.readline

n,m = map(int,input().split())

res = "Yes"
for _ in range(m):
    k = int(input())
    book = list(map(int,input().split()))
    for i in range(1,k):
        if book[i] > book[i-1]:
            res = "No"
print(res)
