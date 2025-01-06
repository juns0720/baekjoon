import sys
input = sys.stdin.readline

n,k = map(int,input().split())
exams = list(map(int,input().split()))

min_score = sys.maxsize

s, e = 0, sum(exams)+1

while s + 1 < e:
    mid = (s + e) // 2
    cnt = 0
    score = 0
    for i in range(n):
        score += exams[i]
        if score >= mid:
            cnt+=1
            score = 0
    if cnt >= k:
        s = mid
    else:
        e = mid
print(s)