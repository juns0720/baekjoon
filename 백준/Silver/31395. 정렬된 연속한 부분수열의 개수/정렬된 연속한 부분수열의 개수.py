import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int,input().split()))



prev = seq[0]
cnt = 1
res = 0
for i in range(1, n):
    if prev < seq[i]:
        cnt += 1
    else:
        res += sum(i for i in range(1,cnt+1))
        cnt = 1
    prev = seq[i]
res += sum(i for i in range(1,cnt+1))

print(res)