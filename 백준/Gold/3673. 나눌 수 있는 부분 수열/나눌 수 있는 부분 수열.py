import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    d,n = map(int,input().split())
    arr = list(map(int,input().split()))

    prefix = [0 for _ in range(n)]
    prefix[0] = arr[0] % d
    dic = dict()
    for i in range(1,n):
        prefix[i] = (prefix[i-1] + arr[i]) % d
    
    res = 0
    for i in range(n):
        if prefix[i] == 0:
            res += 1
        if prefix[i] in dic:
            res += dic[prefix[i]]
            dic[prefix[i]] += 1
        else:
            dic[prefix[i]] = 1
    
    print(res)