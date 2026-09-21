import sys

def solution(arr):
    INF = sys.maxsize
    nums = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    n = len(nums)

    mx = [[-INF] * n for _ in range(n)]
    mn = [[INF] * n for _ in range(n)]
    for i in range(n):
        mx[i][i] = mn[i][i] = nums[i]

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            for k in range(i, j):
                if ops[k] == '+':
                    mx[i][j] = max(mx[i][j], mx[i][k] + mx[k+1][j])
                    mn[i][j] = min(mn[i][j], mn[i][k] + mn[k+1][j])
                else:
                    mx[i][j] = max(mx[i][j], mx[i][k] - mn[k+1][j])
                    mn[i][j] = min(mn[i][j], mn[i][k] - mx[k+1][j])

    return mx[0][n-1]