import sys
input = sys.stdin.readline


N = int(input())
arr = sorted(list(map(int,input().split())))

start = 0
end = 0
res = [int(1e9),int(1e9),int(1e9)]
for i in range(N):
    value = arr[i]
    start = i+1
    end = N-1
    while start < end:
        total_value = value+arr[start]+ arr[end]
        if abs(total_value) < abs(sum(res)):
            res = [arr[i],arr[start],arr[end]]

        if total_value > 0:
            end-=1
        elif total_value < 0:
            start+=1
        else:
            break
print(*res)