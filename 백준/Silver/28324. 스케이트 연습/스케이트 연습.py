import sys
input = sys.stdin.readline

n = int(input())

course = list(map(int,input().split()))

count = 0
res = 0
for point in course[::-1]:
    if point > count:
        count+=1
    count = min(count, point)
    res+=count
print(res)
