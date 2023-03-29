import sys
input = sys.stdin.readline

n = int(input())
#t = [[1,3],[5,5],[3,5],[0,9],[5,7],[3,7],[6,9],[5,9],[8,9],[4,9],[9,9]]
cnt = 1
t = []
for i in range(n):
    t.append(list(map(int,input().split())))
t.sort(key= lambda x : (x[1], x[0]))
start = t[0][0]
end = t[0][1]
for i in range(1,n):
    if t[i][0] >= end:
        start = t[i][0]
        end = t[i][1]
        cnt+=1
print(cnt)
