import sys
input = sys.stdin.readline

Hour,Min,Sec = map(int,input().split())
Sec += int(input())

Min += Sec // 60
Sec %= 60
if Min >=60:
    Hour+=Min//60
    Min %=60
    
if Hour >=24:
    i = Hour//24
    Hour-=24*i

print(Hour, Min, Sec)



