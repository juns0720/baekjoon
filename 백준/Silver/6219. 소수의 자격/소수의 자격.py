import sys
input = sys.stdin.readline

def p():
    board = [i for i in range(b+1)]
    board[1] = 0
    for i in range(2,b+1):
        for j in range(2*i,b+1,i):
            board[j] = 0
    return board



a,b,d = map(int,input().split())
primes = p()
cnt = 0
for i in range(a,b+1):
    if primes[i] and str(d) in str(primes[i]):
        cnt += 1
print(cnt)