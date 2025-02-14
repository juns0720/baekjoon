import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def pre_order(in_s, in_e, post_s, post_e):

    if (in_s > in_e) or (post_s > post_e):
        return
    
    node = post_order[post_e]
    print(node, end = ' ')

    left = in_order_idx[node] - in_s
    right = in_e - in_order_idx[node]

    pre_order(in_s, in_s + left-1, post_s, post_s + left -1)
    pre_order(in_e - right + 1, in_e, post_e - right, post_e -1)

n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
in_order_idx = [0 for _ in range(n+1)]
for i in range(n):
    in_order_idx[in_order[i]] = i
pre_order(0, n-1, 0, n-1)