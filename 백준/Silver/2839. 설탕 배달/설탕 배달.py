import sys
input = sys.stdin.readline

N = int(input())

if N % 5 == 0:
    cnt = N // 5
else:
    cnt = 0
    while N > 0:
        N-=3        #5로 안나눠지니 3개만큼 빼고 5로 나누기
        cnt+=1
        if N % 5 == 0:
            cnt+= N//5
            break
        elif N == 1 or N == 2:
            cnt = -1
            break
        elif N == 0:
            break
print(cnt)


