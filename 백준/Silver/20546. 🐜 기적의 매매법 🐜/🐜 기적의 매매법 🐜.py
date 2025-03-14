import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

jh_money = n
jh_items = 0
sm_money = n
sm_items = 0


for cost in lst:
    # 준현
    if jh_money // cost > 0:
        cnt = jh_money // cost
        jh_items+=cnt
        jh_money -= (cost*cnt)

prev_cost = lst[0]
cnt = 0
seq = 0
#성민
for cost in lst[1:]:
    if cost > prev_cost:
        if seq < 0:
            seq = 0
        seq+=1
    elif cost < prev_cost:
        if seq > 0:
            seq = 0
        seq-=1

    #매수
    if seq <= -3:
        cnt = sm_money // cost
        sm_items += cnt
        sm_money -= (cost*cnt)
    #매도
    if seq >= 3:
        sm_money += (cost*sm_items)
        sm_items = 0
    prev_cost = cost

jh = jh_money + jh_items*lst[-1]
sm = sm_money + sm_items*lst[-1]

if jh > sm:
    print("BNP")
elif jh < sm:
    print("TIMING")
else:
    print("SAMESAME")