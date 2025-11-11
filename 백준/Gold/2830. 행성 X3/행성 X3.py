import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
cnt = [[0,0] for _ in range(21)]
for _ in range(N):
    b = list(bin(int(input()))[2:].zfill(20))
    i = len(b) - 1
    while i > -1:
        if b[i] == '0':
            cnt[len(b)-1-i][0] += 1
        else:
            cnt[len(b)-1-i][1] += 1
        i -= 1
res = 0
for i in range(21):
    res += (cnt[i][0]*cnt[i][1])*(2**i)
print(res)