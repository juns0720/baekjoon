import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = list(map(int,input().split()))
    mid = (arr[0]//2)

    dic = dict()
    for i in arr[1:]:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    arr = list(dic.items())
    arr.sort(key = lambda x : -x[1])
    if arr[0][1] > mid:
        print(arr[0][0])
    else:
        print("SYJKGW")
