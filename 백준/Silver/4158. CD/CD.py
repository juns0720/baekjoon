import sys
input = sys.stdin.readline



def input_cd(n):
    for i in range(n):
        num = int(input())
        if num not in cd:
            cd[num] = 1
            continue
        cd[num]+=1
        pool.add(num)


while True:
    N,K = map(int,input().split())
    if(N,K) == (0,0):
        break
    cd = dict()
    pool = set()

    input_cd(N)
    input_cd(K)
    res = 0

    for i in pool:
        if cd[i] == 2:
            res+=1
    print(res)