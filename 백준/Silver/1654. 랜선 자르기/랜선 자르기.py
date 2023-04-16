import sys

input = sys.stdin.readline

k,n = map(int,input().split())
line = []
for i in range(k):
    line.append(int(input()))
start = 1
end = max(line)
while start <= end:
    Sum = 0
    mid = (start+end)//2
    for i in line:
        Sum +=i//mid
    if Sum == n:
        start = mid+1
    elif Sum > n:
        start = mid+1
    elif Sum < n:
        end = mid-1
print(end)