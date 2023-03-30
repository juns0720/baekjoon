import sys
input = sys.stdin.readline

n = int(input())

list_n = list(map(int,input().split()))
list_n.sort()
time = list_n[0]
Sum = time
for i in range(1,n):
    time = time+list_n[i]
    Sum+=time
print(Sum)