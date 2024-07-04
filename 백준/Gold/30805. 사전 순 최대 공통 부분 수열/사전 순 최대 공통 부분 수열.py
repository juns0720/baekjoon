import sys
input = sys.stdin.readline

lenA = int(input())
lstA = list(map(int,input().split()))

lenB = int(input())
lstB = list(map(int,input().split()))


i = 0
seq = set()
check = [0 for _ in range(lenB)]
for i in range(100,-1,-1):
    for j in range(lenA):
        for k in range(lenB):
            if lstA[j] == lstB[k] == i:
                seq.add((j,i))

seq = sorted(list(seq), key = lambda x: (x[1],-x[0]))




if not seq:
    print(0)
else:
    res = []
    i = len(seq)-1
    start = 0
    max_idx = -1 
    while seq:
        cur_idx, cur_num = seq.pop()
        for i in range(start, lenB):
            if lstB[i] == cur_num and i >= start and max_idx < cur_idx:
                res.append(cur_num)
                start = i+1
                max_idx = cur_idx
                break
    print(len(res))
    print(*res)
