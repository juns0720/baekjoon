import sys
input = sys.stdin.readline

N = int(input())

arr = []
total = 0
mx = 0

for _ in range(N):
    x = int(input())
    total += x
    mx = max(mx, x)

if mx > total - mx:
    print(mx - (total - mx))
else:
    print(total % 2)