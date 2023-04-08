import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = []
B = []
def car(t):
    for i in range(N):
        t.append(list(map(int,input().split())))
car(A)
car(B)

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j],'',end='')
    print()