import sys
input = sys.stdin.readline

N,P = map(int,input().split())

w,l,f = map(int,input().split())
scores = {'W': w, 'L': -l}

p_list = {}
for _ in range(P):
    p = input().strip().split()
    p_list[p[0]] = scores[p[1]]

score = 0
res = "I AM IRONMAN!!"
for _ in range(N):
    p = input().strip()
    if p in p_list:
        score += p_list[p]
    else:
        score -= l
    if score < 0:
        score = 0
    if score >= f:
        res = "I AM NOT IRONMAN!!"
        break
print(res)