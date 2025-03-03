import sys
input = sys.stdin.readline

matrix = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

MOD = 1000000007
N = 8
D = int(input())

def multiply(a,b):
    res = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += a[i][k]*b[k][j]
            res[i][j] %= MOD
    return res

def cal(graph, d):
    if d == 1:
        return graph
    cal2 = cal(graph, d//2)
    if d % 2 == 0:
        return multiply(cal2, cal2)
    else:
        return multiply(multiply(cal2, cal2), graph)

res = cal(matrix, D)
print(res[0][0])