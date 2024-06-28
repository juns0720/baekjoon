import sys
input = sys.stdin.readline

n = int(input())
dic = dict()


for i in range(n):
    fruit, amount  = input().split()
    if fruit not in dic:
        dic[fruit] = int(amount)
    else:
        dic[fruit] += int(amount)

for value in dic.values():
    if value == 5:
        print("YES")
        exit()

print("NO")