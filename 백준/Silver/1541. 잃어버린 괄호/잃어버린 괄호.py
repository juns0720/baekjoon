import sys
input = sys.stdin.readline
formula = input().strip().split('-')
res = 0
for i in formula[0].split('+'):
    res+= int(i)
for i in range(1,len(formula)):
    temp = 0
    for j in formula[i].split('+'):
        temp+= int(j)
    res-=temp
print(res)