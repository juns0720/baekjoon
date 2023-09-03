import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    n = int(input())
    arr = [0 for i in range(n+2)]
    for i in range(2,n+1):
        if arr[i] == 0:
            for j in range(i+i,n+1,i):
                arr[j] = 1
    mid = n//2
    for i in range(mid,-1,-1):
        if arr[i] == 0 and arr[n-i] == 0:
            print(i,n-i)
            break