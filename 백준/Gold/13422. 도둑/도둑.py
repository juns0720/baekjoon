import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    arr = list(map(int,input().split()))*2
    res = 0
    crnt_money = sum(arr[0:m])
    if crnt_money < k:
        res += 1
    if n > m:
        for i in range(m,n+m-1):
            crnt_money += (arr[i] - arr[i-m])
            if crnt_money < k:
                res += 1
    print(res)