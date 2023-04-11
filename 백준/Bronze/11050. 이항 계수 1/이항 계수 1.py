N,K = map(int,input().split())

def fac(N):
    if N == 0:
        return 1
    res = 1
    for i in range(1, N + 1):
        res *= i
    return res


ans = fac(N) //(fac(K) *fac(N-K))
print(ans)
