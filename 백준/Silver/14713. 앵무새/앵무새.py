import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
words = [list(reversed(input().strip().split())) for _ in range(n)]

for i in range(n):
    dic[words[i][-1]] = i
stack = list(reversed(input().strip().split()))

while stack:
    s1 = stack.pop()
    if s1 not in dic:
        print("Impossible")
        exit()
    idx = dic[s1]
    dic.pop(s1)
    words[idx].pop()
    if words[idx]:
        dic[words[idx][-1]] = idx

for word in words:
    if word:
        print("Impossible")
        exit()
print("Possible")