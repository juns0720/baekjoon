import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
cross = list(map(int,input().split()))
left = list(map(int,input().split()))
right = list(map(int,input().split()))

curr_dist =sum(right)

min_cross = 0
min_dist = curr_dist + cross[0]


for i in range(1,n):
    curr_dist = curr_dist + left[i-1] - right[i-1]

    if curr_dist + cross[i] < min_dist:
        min_cross = i
        min_dist = curr_dist + cross[i]

print(min_cross+1,min_dist)