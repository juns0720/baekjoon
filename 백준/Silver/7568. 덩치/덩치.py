import sys
input = sys.stdin.readline

n = int(input())
l = []
ans = []
for i in range(n):
    l.append(list(map(int,input().split())))

for i in range(n): 
    count = 1
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            count+=1
    ans.append(str(count))
print(' '.join(ans))