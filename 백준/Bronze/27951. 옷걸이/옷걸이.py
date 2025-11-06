import sys
input = sys.stdin.readline

n = int(input())
dic = {1: 0, 2: 0, 3: 0}
lst = list(map(int,input().split()))

for i in lst:
    dic[i] += 1

res = []
u,d = map(int,input().split())

for i in lst:
    if i == 1 and dic[i] > 0:
        res.append('U')
        u -= 1
    elif i == 2 and dic[i] > 0:
        res.append('D')
        d -= 1
    elif i == 3:
        if u  > 0:
            res.append('U')
            u -= 1
        elif d > 0:
            res.append("D")
            d -= 1
if u < 0 or d < 0:
    print("NO")
else:
    print("YES")
    print(''.join(res))
