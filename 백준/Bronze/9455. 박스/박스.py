import sys
input = sys.stdin.readline

for tc in range(int(input())):
    m,n = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(m)]
    res = 0
    for col in range(n):
        s = -1
        for row in range(m-1,-1,-1):
            if box[row][col] == 1:
                if s == -1:
                    s = m-1
                    res+=(m-1-row)
                else:
                    res+=(s-1-row)
                    s-=1
    print(res)