import sys
input = sys.stdin.readline


n = int(input())

if n == 1:
    print(0)
    exit()
key = 1
lst = []
for _ in range(n):
    lst.append(int(input()))
cnt = 0



while True:
    max_n = -1
    max_idx = -1
    #맥스 값 구하기
    for i in range(1,n):
        if lst[i] > max_n:
            max_idx = i
            max_n = lst[i]
    if lst[max_idx] < lst[0]:
        break
    else:
        lst[0]+=1
        lst[max_idx]-=1
        cnt+=1

print(cnt)