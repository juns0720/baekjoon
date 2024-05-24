import sys
input = sys.stdin.readline

n = int(input())
al = []

for i in range(n):
    al.append(list(input().split()))
al.sort()
start = 0
end = 0
name = al[0][0]
for i in range(len(al)):
    if al[i][0] != name:
        end = i-1
        for j in range(end, start-1,-1):
            print(name, al[j][1])
        name = al[i][0]
        start = i
for i in range(len(al)-1, start-1,-1):
    print(name, al[i][1])


