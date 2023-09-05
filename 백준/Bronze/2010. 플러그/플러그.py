import sys
input = sys.stdin.readline

N = int(input())
sum = -(N-1)

for i in range(N):
    sum+=int(input())
print(sum)