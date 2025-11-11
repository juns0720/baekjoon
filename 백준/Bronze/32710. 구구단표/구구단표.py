import sys
input = sys.stdin.readline

n = int(input())

s = set()
for i in range(2,10):
    for j in range(1,10):
        s.add(i)
        s.add(j)
        s.add(i*j)
        
print(int(n in s))