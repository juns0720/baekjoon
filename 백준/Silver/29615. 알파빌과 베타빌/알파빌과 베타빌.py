import sys
input = sys.stdin.readline

N,M = map(int,input().split())
line = list(map(int,input().split()))
friend = set(map(int,input().split()))

max_cnt = len(friend)

for i in range(len(friend)):
    if line[i] in friend:
        max_cnt-=1
print(max_cnt)