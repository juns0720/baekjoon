import sys
input = sys.stdin.readline

N = int(input())
line = []
people = set()



for _ in range(N):
    num = int(input())
    line.append(num)
    people.add(num)
res = 0
for i in range(len(line)):
    cnt = 1
    other = set()
    for j in range(i+1, len(line)):
        if line[i] == line[j]:
            if len(other) <= 1:
                cnt+=1
            else:
                break
        else:
            other.add(line[j])
    res = max(res,cnt)
print(res)