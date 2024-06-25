import sys
input = sys.stdin.readline

n,k,m = map(int,input().split())


foods = []
for i in range(n):
    food = int(input())
    if food - k*2 >= 0:
        if food-k*2 == 0:
            continue
        foods.append(food-k*2)
    elif food - k > 0:
            foods.append(food-k)
if not foods:
    print(-1)
else:
    res = -1
    start = 1
    end = max(foods)
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for food in foods:
            cnt += (food // mid)
        if cnt >= m:
            res = max(res, mid)
            start = mid+1
        else:
            end = mid-1
    print(res)



