import sys
input = sys.stdin.readline

for i in range(int(input())):
    R,S = input().split()
    S = list(S)
    P = ''
    for i in S:
        P += i*int(R)
    print(P)

