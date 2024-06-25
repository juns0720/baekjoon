import sys

dic = dict()

n,m = map(int,input().split())

for i in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    if word not in dic:
        dic[word] = 1
    else:
        dic[word]+=1
dic = list(dic.items())

dic.sort(key = lambda x: (-x[1] ,-len(x[0]), x[0]))

for i in dic:
    print(i[0]) 
