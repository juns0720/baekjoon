import sys
input = sys.stdin.readline

N,K = map(int,input().split())

i = 9
n = 1

while True:
    if K > 9*(10**(n-1))*n:
        K -= 9*(10**(n-1))*n
        n += 1
    else:
        break

num = 10**(n-1) + ((K-1) // n) # 현재 숫자
if num > N:
    print(-1)
else:
    num = list(str(num))
    idx = (K-1) % n # 자리수
    print(num[idx])