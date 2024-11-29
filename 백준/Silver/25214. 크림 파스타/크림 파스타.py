import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))


min_value = lst[0]
max_value = 0
print(max_value, end= ' ')
for i in range(1, n):
    min_value = min(min_value, lst[i])
    max_value = max(max_value,lst[i]-min_value)
    print(max_value, end = ' ')