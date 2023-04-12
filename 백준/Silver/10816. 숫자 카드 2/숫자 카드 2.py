import sys
import collections
input = sys.stdin.readline

N = int(input())
Nl = list(map(int,input().split()))
Nl.sort()
M = int(input())
Ml = list(map(int,input().split()))
res_dic = collections.Counter(Nl)
for val in Ml:
    if val in res_dic:
        print(res_dic[val],end=' ')
    else:
        print(0,end=' ')
