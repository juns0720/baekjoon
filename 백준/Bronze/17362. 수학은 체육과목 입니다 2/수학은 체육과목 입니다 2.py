import sys
input = sys.stdin.readline

n = int(input())

if n % 8 == 1:
    print(1)
elif n % 8 == 5:
    print(5)
elif n % 4 == 3:
    print(3)
elif n % 8 in [0,2]:
    print(2)
else:
    print(4)