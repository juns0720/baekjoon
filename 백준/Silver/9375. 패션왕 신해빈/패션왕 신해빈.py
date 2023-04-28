import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    wear = dict()
    for j in range(N):
        s = input().split()
        if s[1] in wear:
            wear[s[1]].append(s[0])
        else:
            wear[s[1]]=[s[0]]
    cnt = 1
    for i in wear:
        cnt*=(len(wear[i])+1)
    print(cnt-1)
