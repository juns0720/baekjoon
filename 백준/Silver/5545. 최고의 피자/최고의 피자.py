import sys
input = sys.stdin.readline

N = int(input())
A,B = map(int,input().split())
C = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse = True)


def cal(n,total):
    return total // n
#i개 토핑
total = C
res = cal(A,total)
for i in range(N):
    total += arr[i]
    cur_res = cal(A + B*(i+1),total)
    if res > cur_res:
        break
    else:
        res = cur_res
print(res)