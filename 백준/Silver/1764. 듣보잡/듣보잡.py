import sys
input = sys.stdin.readline

N,M = map(int,input().split())
man1 = set()
man2 = set()
for i in range(N):
    name = input().strip()
    man1.add(name)
for i in range(M):
    name = input().strip()
    man2.add(name)

man_list = list(man1 & man2)
print(len(man_list))
for name in sorted(man_list):
    print(name)
