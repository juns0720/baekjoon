import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

length = len(S)
res = 26+25*(length)
print(res)