import sys
input = sys.stdin.readline

for tc in range(int(input())):
    a,b = map(int,input().split())
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
    print(10*a)