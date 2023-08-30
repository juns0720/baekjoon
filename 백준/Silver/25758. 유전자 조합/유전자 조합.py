import sys
import itertools
input = sys.stdin.readline

n = int(input())
l = list(input().split())
q = ''
set1 = set()
arr = []
if n < 353:
    for i in list(set(itertools.permutations(l,2))):
        s = i[0]+i[1]
        q+=(max(s[0]+s[3]))
    print(str(len(set(q)))+'\n'+' '.join(sorted(set(q))))
else:
    for i in l:
        arr.append(i[0])
        arr.append(i[1])
    arr.sort()
    for i in range(2):
        del arr[0]
    arr = list(set(arr))
    print(len(arr))
    for i in sorted(arr):
        print(i,end=' ')