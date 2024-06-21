import sys

input = sys.stdin.readline
n = int(input())

dict = dict()
for i in range(n):
    s1 = input().strip()
    if s1 not in dict:
        dict[s1] = 1
    else:
        dict[s1]+=1
res = list(sorted(dict.items(), key = lambda x: (-x[1],x[0])))
print(res[0][0])
