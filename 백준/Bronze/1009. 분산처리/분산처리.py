import sys
input = sys.stdin.readline
n = int(input())
answer = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    b = b%4
    if b%4 ==0 :
        b = 4
    tmp = a**b%10
    if tmp == 0:
        print(10)
    else:
        print(tmp)