import sys
input = sys.stdin.readline

lst = [[0],[4,5],[-1],[4,5],[2,3],[8],[2,3],[8],[6,7]]



def check(arr):
    prev = arr[0]
    for i in range(1,len(arr)):
        if arr[i] not in lst[prev]:
            return "NOT"
        prev = arr[i]
    return "VALID"

tc = 1
while True:

    arr = list(map(int,input().strip()))
    if arr == [0]:
        break
    if arr[0] != 1 or arr[-1] != 2:
        res = "NOT"
    else:
        res = check(arr)
    print(str(tc)+'. '+res)
    tc+=1


