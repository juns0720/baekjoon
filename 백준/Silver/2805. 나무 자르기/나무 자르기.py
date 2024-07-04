import sys
input = sys.stdin.readline


n,m = map(int,input().split())
trees = list(map(int,input().split()))

def cal_height(height):
    sum_height = 0
    for tree in trees:
        cur_height = tree - height
        if cur_height > 0:
            sum_height += cur_height
    return sum_height

s = 0
e = max(trees)

while s < e:
    mid = (s + e)//2
    cur_height = cal_height(mid)
    if cur_height < m:
        e = mid
    elif cur_height == m:
        break
    else:
        if s == mid:
            break
        s = mid
print(mid)