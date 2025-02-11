import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append(a-b)
arr.sort()

if n%2 == 1:
    print(1)
else:
    print(abs(arr[n//2] - arr[n//2-1]) + 1)