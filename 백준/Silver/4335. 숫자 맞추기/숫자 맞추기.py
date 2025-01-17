import sys
input = sys.stdin.readline

cache = [0 for _ in range(11)]
res = "Stan may be honest"
while True:
    num = int(input())
    if not num:
        break
    ans = input().strip()
    if ans == "too high":
        for i in range(num, 11):
            cache[i] = 1
    elif ans == "too low":
        for i in range(1,num+1):
            cache[i] = 1
    else:
        if cache[num]:
            res = "Stan is dishonest"
        print(res)
        cache = [0 for _ in range(11)]
        res = "Stan may be honest"