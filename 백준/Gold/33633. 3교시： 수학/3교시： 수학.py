import sys
input = sys.stdin.readline

N = int(input())

res = []

def solve(i, n):
    global res
    if i == 1:
        res.append(n)
        return
    
    A0 = 2*n
    A1 = (n-1) / 3

    if A0 != 1 and A0 % 2 == 0:
        solve(i-1, A0)
    if A1 != 1 and A1 % 2 == 1:
        solve(i-1, int(A1))

solve(N, 1)
res.sort()

print(len(res))
for i in res:
    print(i)