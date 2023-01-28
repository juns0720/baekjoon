import sys
input = sys.stdin.readline

n = int(input())

a = []
t = []
s= set()
for i in range(n):
    a.append(input())

for i in a:
    i = i.strip()
    s.add(i)

for i in s:
    t.append(i)
t.sort()
t.sort(key = len)

for i in t:
    print(i)