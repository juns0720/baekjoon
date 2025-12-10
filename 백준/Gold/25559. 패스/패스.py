import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
    exit()
    
if N % 2 == 0:
    res = [N, N-1]
    even = 0
    odd = N-1
    for i in range(2,N):
        if i % 2 == 0:
            even += 2
            res.append(even)
        else:
            odd -= 2
            res.append(odd)
    
    print(*res)
else:
    print(-1)