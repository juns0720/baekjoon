import sys
input = sys.stdin.readline

def binary_search(target, arr, skip1, skip2):
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if mid == skip1 or mid == skip2:
            if mid < skip1:
                s = mid + 1
            else:
                e = mid - 1
            continue

        if arr[mid] < target:
            s = mid + 1
        elif arr[mid] > target:
            e = mid - 1
        else:
            return True
    return False

N = int(input())
arr = sorted(list(map(int, input().split())))
res = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        target = arr[i] - arr[j]
        if binary_search(target, arr, i, j):
            res += 1
            break
print(res)
