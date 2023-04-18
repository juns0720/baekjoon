import sys
input = sys.stdin.readline

L,P = map(int,input().split())
people = L*P
news = list(map(int,input().split()))

for i in news:
    print(i - people,end=' ')

    