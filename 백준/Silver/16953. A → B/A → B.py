import sys
input = sys.stdin.readline

A,B = map(int,input().split())
cnt = 0

while True:
    if A == B:
        print(cnt+1)
        break
    elif  A > B:
        print(-1)
        break
    B = str(B)
    if B[-1] != '1' and int(B[-1]) %2 == 1:
        print(-1)
        break
    elif B[-1] == '1':
        bl = []
        for i in str(B):
            bl.append(i)
        bl.pop()
        B = int(''.join(bl))
        cnt+=1
    else:
        B = (int(B)//2)
        cnt+=1


