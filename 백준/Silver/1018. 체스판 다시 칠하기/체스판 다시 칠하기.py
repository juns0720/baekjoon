import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
chess = []
for i in range(n[0]):       #체스판 만들기.
    s = input().strip()
    chess.append(list(s))

last = 64   # 최댓값
cntx,cnty,cnt = 0,0,0
while True:
    for b in range(8):
        for a in range(8):
            y = b+cnty
            x = a+cntx
            if x > cntx+7 or cnty == n[0]-7:
                break
            if (x+y)%2 == 0:
                if chess[y][x] !='W':
                    cnt+=1
            elif (x+y)%2 == 1:
                if chess[y][x] != 'B':
                    cnt+=1
    if cnty == n[0]-7:
        break
    if cnt<last:
        last = cnt
    cnt = 0
    cntx += 1
    if cntx+7 > n[1]-1:
        cntx = 0
        cnty += 1
cntx,cnty,cnt = 0,0,0
while True:
    for b in range(8):
        for a in range(8):
            y = b+cnty
            x = a+cntx
            if x > cntx+7 or cnty == n[0]-7:
                break
            if (x+y)%2 == 0:
                if chess[y][x] !='B':
                    cnt+=1
            elif (x+y)%2 == 1:
                if chess[y][x] != 'W':
                    cnt+=1
    if cnty == n[0]-7:
        break
    if cnt<last:
        last = cnt
    cnt = 0
    cntx += 1
    if cntx+7 > n[1]-1:
        cntx = 0
        cnty += 1
print(last)
