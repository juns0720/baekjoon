import sys

input = sys.stdin.readline

while True:
    try:
        n,m = map(int,input().split())
    except:
        break
    cnt = 0
    for num in range(n, m+1):
        nlist = list(str(num))
        tmp1 = len(nlist)
        tmp2 = len(set(nlist))
        if(tmp1 == tmp2):
            cnt+=1
    print(cnt)