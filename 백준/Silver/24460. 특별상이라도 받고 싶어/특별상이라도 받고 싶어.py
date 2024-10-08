import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]


def recursion(n, row,col):
    if n == 1:
        return arr[row][col]
    else:
        tmp1 = []
        
        tmp1.append(recursion(n//2, row,col)) 
        tmp1.append(recursion(n//2, row ,col + n//2))
        tmp1.append(recursion(n//2 , row + n//2 ,col ))
        tmp1.append(recursion(n//2 , row + n//2,col + n//2))
        return sorted(tmp1)[1]

print(recursion(N, 0,0))