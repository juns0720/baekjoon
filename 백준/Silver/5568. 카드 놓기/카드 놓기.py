import sys
import itertools
input = sys.stdin.readline

n = int(input())
k = int(input())
nl = []
ans = set()
for i in range(n):
    s = input().strip()
    nl.append(s)

for i in set(itertools.permutations(nl,k)):
    ans.add(''.join(i))
print(len(ans))



