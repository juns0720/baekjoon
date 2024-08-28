import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())
    flag = 1
    for i in range(2, 10**6+1):
        if num % i == 0:
            flag = 0
            break
    print("YES") if flag else print("NO")