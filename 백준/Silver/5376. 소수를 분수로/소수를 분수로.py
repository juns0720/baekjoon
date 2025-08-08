import sys
from math import gcd
input = sys.stdin.readline

for tc in range(int(input())):
    dcm = list(input().strip())
    front = ['0']
    front_cnt = 0
    for i in range(2,len(dcm)):
        if dcm[i] == '(':
            cycle = ''.join(dcm[i+1:-1])
            break
        front.append(dcm[i])
        front_cnt += 1
    else:
        a = int(''.join(front))
        b = 10**front_cnt
        c = gcd(a,b)
        print(f'{a//c}/{b//c}')
        continue

    a = int(''.join(front) + cycle)- int(''.join(front))
    b = int('9'*len(cycle)+'0'*front_cnt)
    c = gcd(a, b)
    print(f'{a//c}/{b//c}')
