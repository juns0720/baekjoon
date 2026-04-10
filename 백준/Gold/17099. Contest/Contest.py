import sys
input = sys.stdin.readline

n = int(input())

arr = [[0,0,0]]

for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x: (x[1]))

end = [arr[i][1] for i in range(n+1)]

dp = [0 for _ in range(n+1)]
def binary_search(idx, target):
    s = 0
    e = idx
    
    while s+1 < e:
        mid = (s + e) // 2
        
        if end[mid] < target:
            s = mid
        else:
            e = mid
    return s

for i in range(1, n+1):
    j  = binary_search(i, arr[i][0])
    dp[i] = max(arr[i][2] + dp[j], dp[i-1])

print(dp[-1])