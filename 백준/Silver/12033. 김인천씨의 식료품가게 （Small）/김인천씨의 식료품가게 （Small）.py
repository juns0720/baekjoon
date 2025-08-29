import sys
input = sys.stdin.readline

for tc in range(1,int(input())+1):
    N = int(input())
    dic = dict()
    arr = list(map(int,input().split()))
    for i in arr:
        if i in dic:
            dic[i] += 1
        else: 
            dic[i] = 1
    res = []
    cnt = 0
    for i in arr:
        if cnt == N:
            break
        price = i*4//3
        if price in dic and dic[price] > 0 and dic[i] > 0:
            dic[price] -= 1
            dic[i] -= 1
            res.append(str(i))
            cnt += 1
    s = ' '.join(res)
    print(f'Case #{tc}: {s}')