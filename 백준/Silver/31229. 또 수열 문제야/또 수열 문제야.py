import sys
input = sys.stdin.readline

N = int(input())
res = [1]
for i in range(N-1):
    for j in range(res[i]+1,10**9+1):
        can = 0
        for k in res:
            if k*j % (k+j) == 0:
                break
        else:
            can = 1
        if can:
            res.append(j)
            break
print(*res)