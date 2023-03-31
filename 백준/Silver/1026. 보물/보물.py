import sys
input = sys.stdin.readline


n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
B.reverse()
Sum = 0
for i in range(n):
    Sum += A[i]*B[i]
print(Sum)