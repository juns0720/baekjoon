"""
1. 문자열의 뒤에 A를 추가한다.
2. 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.


A -> BA -> BAB -> BABA

반대로 돌아가기
BABA -> BAB (뒤에 A 제거)
BAB -> BA (앞에 B 삭제 후 뒤집기)
BA -> A (앞에 B 삭제 후 뒤집기)

1. 뒤에 A를 삭제한다.
2. 앞에 B를 삭제 후 뒤집는다.
"""
import sys
from collections import deque
input = sys.stdin.readline

def recursion(t):
    if S == list(t):
        print(1)
        exit()

    if len(t) == 0:
        return

    if t[-1] == 'A':
        recursion(t[:-1])
    if t[0] == 'B':
        recursion(t[1:][::-1])


S = list(input().strip())
T = list(input().strip())
recursion(T)
print(0)
