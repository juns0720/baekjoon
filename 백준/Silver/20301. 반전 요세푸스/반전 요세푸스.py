import sys
input = sys.stdin.readline
n,k,m = map(int,input().split())
arr = [i for i in range(1,n+1)]

i = k-1
print(arr.pop(i))

c = 1
while arr:
    if c // m % 2 == 0:
        i = (i+(k-1)) % len(arr)
    else:
        i = (i-k) % len(arr)

    print(arr.pop(i))
    c += 1