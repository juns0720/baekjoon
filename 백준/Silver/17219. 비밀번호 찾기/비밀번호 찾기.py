import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
dic = {}
for i in range(n[0]):
    s = input().split()
    dic[s[0]] = s[1]
for i in range(n[1]):
    s = input().strip()
    print(dic[s])
