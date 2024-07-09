import sys
input = sys.stdin.readline

N = int(input())
fruits = list(map(int,input().split()))
exist = [0 for _ in range(10)]
start = 0
end = 0
max_res = -1
exist[fruits[start]] = 1
cur_cnt = 1
cur_len = 1
while end < N:
    end+=1
    if end < N:
        if exist[fruits[end]] == 0:
            cur_cnt+=1
        exist[fruits[end]]+=1
        cur_len+=1

    if cur_cnt < 3:
        max_res = max(max_res,cur_len)
    else:
        if exist[fruits[start]] == 1:
            cur_cnt-=1
        exist[fruits[start]]-=1
        start+=1
        cur_len-=1
print(max_res)