import sys
input = sys.stdin.readline

n = int(input())

price = [list(map(int,input().split())) for _ in range(n)]
price.sort(key = lambda x: x[0])
max_price = 0
max_revenue = 0

for i in range(n): # i번째 물건의 가격으로 설정
    total_revenue = max(0 , price[i][0] - price[i][1]) # 현재 물건으로 낼 수 있는 총 수익
    now_item_price = price[i][0] #기준 물건의 가격

    for j in range(i+1,n): # i+1번째 물건부터 넣을 수 있는지 탐색
        rev2 = max(0, now_item_price - price[j][1]) #기준 물건을 기준으로 가치 판단
        total_revenue += rev2
    if total_revenue > max_revenue:
        max_price = price[i][0]
        max_revenue = total_revenue
print(max_price)