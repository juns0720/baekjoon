import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []

def recursion(cnt, start):
    if cnt == M:
        print(' '.join(arr))
        return
    for i in range(1,N+1):
        if str(i) not in arr:
            arr.append(str(i))
            recursion(cnt+1, start+1)
            arr.pop()
            
recursion(0,1)