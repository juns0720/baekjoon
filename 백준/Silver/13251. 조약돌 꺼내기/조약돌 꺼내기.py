import sys
input = sys.stdin.readline



def cal(num, k):
    res = 1
    for i in range(k):
        if num <= 0:
            return 0
        res*=num
        num-=1
    return res


M = int(input())

stones = list(map(int,input().split()))
K = int(input())
parent = cal(sum(stones),K)
son = 0
for stone in stones:
    son+=cal(stone,K)
res = son/parent
print(res)