import sys
input = sys.stdin.readline

min = list(map(int,input().split()))
man = list(map(int,input().split()))

if sum(min) > sum(man) or sum(min) == sum(man):
    print(sum(min))
else:
    print(sum(man))
