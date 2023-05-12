import sys
input = sys.stdin.readline

A,B = map(int,input().split())
M = (B-A)/400
wook_rate = 1/(1+10**M)

print(wook_rate)