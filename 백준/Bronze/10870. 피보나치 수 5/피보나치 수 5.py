import sys
input = sys.stdin.readline

n = int(input())
b = 0
a = 1
if n == 0:
    print(b)
else:
    while n > 1:
        temp = a
        a = b+a
        b = temp
        n-=1   
    print(a)