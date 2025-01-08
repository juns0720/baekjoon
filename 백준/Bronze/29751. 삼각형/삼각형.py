import sys
input = sys.stdin.readline

w,h = map(int,input().split())

res =  (w*h)/2

print(f'{res:0.1f}')