import sys
input = sys.stdin.readline

def hanoi(n,b,a,m):
    if n == 0:
        return
    hanoi(n-1,b,m,a)
    print(b, a)
    hanoi(n-1,m,a,b)
    

n = int(input())

print(2**n - 1)
hanoi(n,1,3,2)
