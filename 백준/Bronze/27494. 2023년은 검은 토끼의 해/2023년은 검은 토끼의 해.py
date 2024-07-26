import sys
input = sys.stdin.readline

N = int(input())

serial = ['2','0','2','3']
cnt = 0
def check(num):
    idx = 0
    for i in str(num):
        if idx == 4:
            return 1
        if i == serial[idx]:
            idx+=1
    if idx == 4:
        return 1
    return 0

for num in range(2022,N+1):
    cnt += check(num)
print(cnt)