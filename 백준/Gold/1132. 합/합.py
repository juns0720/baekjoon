import sys
input = sys.stdin.readline

n = int(input())

apb = {}

res = 0

apb = {}
cant = set()
total = set()
lst = [list(input().strip()) for _ in range(n)]

for num in lst:
    value = 1
    for i in range(len(num)-1,-1,-1):
        if num[i] not in apb:
            apb[num[i]] = value
        else:
            apb[num[i]] += value

        if i == 0:
            cant.add(num[i])
        total.add(num[i])
        value *= 10

sorted_apb = sorted(apb.items(), key = lambda x:x[1])

num = 9

seq = {}
if len(total) == 10:
    for i in sorted_apb:
        if i[0] not in cant:
            seq[i[0]] = 0
            break
        
for i in reversed(sorted_apb):
    if i[0] not in seq:
        seq[i[0]] = num
        num-=1
res = 0
for i in seq.items():
    res += apb[i[0]] * seq[i[0]]
print(res)