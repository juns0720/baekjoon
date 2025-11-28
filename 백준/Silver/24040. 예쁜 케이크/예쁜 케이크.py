import sys
import math
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    if N % 9 == 0 or N % 3 == 2:
        print("TAK")
    else:
        print("NIE")
