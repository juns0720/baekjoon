import sys
input = sys.stdin.readline

n = int(input())
time = sorted([list(map(int,input().split())) for _ in range(n)], key = lambda x: (x[1], -x[0]))

s,e = time[0][1]-time[0][0], time[0][1]

for i in range(1,n):
    if s < 0:
        s = -1
        break
        
    hour, ne = time[i]

    r = (e + hour) - ne
    if r < 0:
        e += hour
    else:
        e = ne
        s -= r
        
        if s < 0:
            s = -1
            break

print(s)