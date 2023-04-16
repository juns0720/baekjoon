import sys
input = sys.stdin.readline

A,B,C =map(int,input().split())
Sum = A
revenue = 0
res = 0
if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)