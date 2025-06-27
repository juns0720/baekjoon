import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0 or n % 5 == 0:
    print(-1)
    exit()

num = 1
cnt = 1

while True:
    if num % n == 0:
        break
    num = ((num*10) + 1) % n
    cnt += 1
print(cnt)