import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    s = list(input().strip())
    for i in range(len(s)-2,-1,-1):
        tmp = []
        for j in range(i+1, len(s)):
            if s[j] > s[i]:
                tmp.append((s[j],j))
        if tmp:
            idx = sorted(tmp)[0][1]
            s[i], s[idx] = s[idx], s[i]
            s[i+1:] = sorted(s[i+1:])
            break
    print(''.join(s))