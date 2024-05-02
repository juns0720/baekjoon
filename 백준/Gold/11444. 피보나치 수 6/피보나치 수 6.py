import sys
input = sys.stdin.readline


def cal_odd():
    ##현재 좌표
    tmp_list = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            tmp = 0
            for i in range(n):
                    tmp+=result[row][i]*matrix[i][col]
            tmp_list[row][col] = tmp % 1000000007
    for row in range(n):
        for col in range(n):
            result[row][col] = tmp_list[row][col]

def cal_even():
    
    tmp_list = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            tmp = 0
            for i in range(n):
                    tmp+=result[row][i]*result[i][col]
            tmp_list[row][col] = tmp % 1000000007
    for row in range(n):
        for col in range(n):
            result[row][col] = tmp_list[row][col]


def devide(depth):
    if depth == 1:
        return
    else:
        devide(depth//2)
        cal_even()
        if depth % 2 == 1:
            cal_odd()

   

     
depth = int(input())
n = 2
matrix = [[1,1],[1,0]]
result = [[1,1],[1,0]]

devide(depth)
print(result[1][0])