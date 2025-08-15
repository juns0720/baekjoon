import sys
input = sys.stdin.readline

for tc in range(int(input())):
    s = list(input().strip())

    cnt = 0
    while True:
        s1 = sorted(s, reverse = True)
        s2 = sorted(s)
        res = int(''.join(s1)) - int(''.join(s2))
        if 6174 == int(''.join(s)):
            break
        else:
            s = list(str(res).strip())
            if len(s) < 4:
                s = (4-len(s))*['0'] + s
            cnt += 1
    print(cnt)