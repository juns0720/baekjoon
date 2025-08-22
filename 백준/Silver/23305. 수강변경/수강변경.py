import sys
input = sys.stdin.readline

N = int(input())
dic = dict()
for i in list(map(int,input().split())):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in list(map(int,input().split())):
    if i in dic and dic[i] > 0:
        dic[i] -= 1
        N -= 1

print(N)