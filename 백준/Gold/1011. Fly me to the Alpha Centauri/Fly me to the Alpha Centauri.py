import sys
input = sys.stdin.readline

for t in range(int(input())):
    x,y = map(int,input().split())

    dist = y-x
    i = 1
    cnt = 0
    while True:
        if dist <= 0:
            break
        elif dist-i <= 0:
            cnt += 1
            break
        
        dist -= 2*i
        i += 1
        cnt += 2
    print(cnt)