import sys
input = sys.stdin.readline

n = int(input())
nl = input().split()
nd = {}
a = 0
for i in range(n):
    nd[nl[i]] = 0
for i in range(n):
    s =  input().split()
    for i in s:
        for key, value in nd.items():
            if key == i:
                nd[i]+=1
nd1 = dict(sorted(nd.items(), key = lambda x:x[1], reverse = True))
for i,v in nd1.items():
    print(i, v)