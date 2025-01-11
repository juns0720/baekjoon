import sys
input = sys.stdin.readline

dic = dict()
total = 0
while True:
    tree = input().strip()
    if not tree:
        break
    if tree in dic:
        dic[tree] += 1
    else:
        dic[tree] = 1
    total += 1
trees = sorted(list(dic.keys()))
for tree in trees:
    print(f'{tree}{dic[tree]/total*100 : .04f}')