import sys
from math import log2
input = sys.stdin.readline
k = int(input())

check = 0
rv = 0
while k > 2:

    if k > 1 and k&(k-1)==0:
        check = 1
        if int(log2(k)) % 2 == 0:
            print(0+rv, end = ' ')
            break
        else:
            print((1+rv)%2, end = ' ')
            break
        
    pow = int(log2(k))
    k -= 2**pow
    rv = (rv + 1)%2
if not check:
    print(0+rv if k == 1 else (1+rv)%2, end = ' ')
