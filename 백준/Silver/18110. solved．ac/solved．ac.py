import sys
import math
input = sys.stdin.readline

def Round(n):
    a = n-math.floor(n)
    if a >= 0.5:
        return math.ceil(n)
    else:
        return math.floor(n)
    
num = []
n = int(input())
for _ in range(n):
    num.append(int(input()))
if n == 0:
    print(0)
else:
    per = (Round(n*0.15))
    print(Round((sum(sorted(num)[per:n-per])) / (n-2*per)))