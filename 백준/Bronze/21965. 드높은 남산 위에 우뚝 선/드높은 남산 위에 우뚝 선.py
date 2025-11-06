import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

i = 1
while i < n:
    if lst[i-1] == lst[i]:
        print("NO")
        exit()
    elif lst[i] < lst[i-1]:
        i+=1
        break
    i += 1

while i < n:
    if lst[i-1] <= lst[i]:
        print("NO")
        exit()
    i += 1
print("YES")
        