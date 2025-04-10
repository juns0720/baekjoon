import sys
from math import log2
input = sys.stdin.readline
MAX = int(log2(500000)) + 1

m = int(input())
seq = [0] + list(map(int,input().split()))



sparse = [[0 for _ in range(m+1)] for _ in range(MAX+1)]
for i in range(1,m+1):
    sparse[1][i] = seq[i]

for i in range(2,MAX+1):
    for j in range(1,m+1):
        sparse[i][j] = sparse[i-1][sparse[i-1][j]]

def find_value(n,x):
    while n > 0:
        target = int(log2(n)) + 1
        x = sparse[target][x]
        n -= 2**(target-1)
    return x


for q in range(int(input())):
    n,x = map(int,input().split())
    print(find_value(n,x))
