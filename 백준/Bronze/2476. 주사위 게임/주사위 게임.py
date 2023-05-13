import sys
input = sys.stdin.readline

n = int(input())
price = 0
for i in range(n):
    a,b,c = map(int,input().split())

    if a == b and b == c:
        price = max(price,10000 + a * 1000)
    elif a == b:
        price = max(price,1000 + a*100)
    elif b == c:
        
        price = max(price,1000 + b*100)
    elif a == c:
        price = max(price,1000 + c*100)
    else:
        price = max(price,max(a,b,c)*100)
print(price)