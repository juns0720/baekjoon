import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

def init_array(s, e, arr):
    for i in range(s,e):
        arr.append(tmp[i])

for k in range(int(input())):
    A = deque()
    B = deque()
    tmp = list(map(int,input().split()))

    init_array(0, 4, A)
    init_array(4, 8, B)
    ans = 0
    for _ in range(4):
        B.rotate(-1)
        B[1], B[2] = B[2], B[1]
        for i in range(4):
            if A[i] == B[i]:
                tmp_A = deque()
                tmp_B = deque()
                for j in range(4):
                    if i == j:
                        continue
                    tmp_A.append(A[j])
                    tmp_B.append(B[j])
                for i in range(3):
                    tmp_A.rotate(1)
                    if tmp_A == tmp_B:
                        ans = 1
                        break
    print(ans)