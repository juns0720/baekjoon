import sys
input = sys.stdin.readline

def binary_search(s,e, target):

    while s + 1 < e:
        mid = (s + e) // 2
        
        if lst[mid] < target:
            s = mid
        else:
            e = mid
    
    return e

while True:
    try:
        N = int(input())
        arr = list(map(int,input().split()))
    except:
        exit()

    lst = [arr[0]]
    for i in range(1,N):
        idx = binary_search(-1,len(lst)-1, arr[i])
        if lst[idx] < arr[i]:
            lst.append(arr[i])
        else:
            lst[idx] = arr[i]
    print(len(lst))