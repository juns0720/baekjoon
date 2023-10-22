import sys
input = sys.stdin.readline

for i in range(int(input())):
    ac = input().strip()
    n = int(input())
    tmp = input().strip()
    if n == 0:
        arr = []
    else:
        arr = tmp[1:-1].split(',')
    start = 0
    end = len(arr)
    vec = 0     # 0 = 정방향, 1 = 역방향
    # arr[start:end] = arr[0:4]
    err = False
    for i in range(len(ac)):
        if ac[i] == 'R':
            vec = (vec+1)%2
        elif ac[i] == 'D':
            if len(arr) == 0 or start >= end:
                err = True
                break
            if vec == 0:
                start+=1
            elif vec == 1:
                end-=1

    if err == True:
        print('error')
    else:
        print('[',end='')
        if vec == 0:
            print(*arr[start:end],sep=',',end='')
        elif vec == 1:
            print(*list(reversed(arr[start:end])),sep=',',end='')
        print(']')