import sys
from itertools import product
input = sys.stdin.readline

a_channel = ['0','1','2','3','4','5','6','7','8','9']
num = input().strip()
N = int(input())
if N == 0:
    d_channel = []
else:
    d_channel = list(input().strip())
channel = [i for i in a_channel if i not in d_channel]

if num == '100':
    print(0)
else:
    Min = abs(100-int(num))
    for j in range(1,len(num)+2):
        for i in product(channel,repeat = j):
            val = ''.join(i)
            Min = min(Min,abs(int(num) - int(val))+len(str(int(val))))
    print(Min)