import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr = list(input().strip())

def cal(x):
    Min = x-K
    Max = x+K
    if Min < 0:
        Min = 0
    if Max > N-1:
        Max = N-1
    for i in range(Min,x):
        if arr[i] == 'H':
            arr[i] = 'X'
            return 1
    for i in range(x,Max+1):
        if arr[i] == 'H':
            arr[i] = 'X'
            return 1
    return 0

Sum = 0
for i in range(len(arr)):
    if arr[i] == 'P':
        Sum+=cal(i)
print(Sum)
