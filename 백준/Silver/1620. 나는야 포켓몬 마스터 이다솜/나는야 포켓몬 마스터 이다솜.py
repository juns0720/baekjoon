import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pkmon_id = dict()
pkmon_num = dict()

for i in range(1,N+1):
    t = input().strip()
    pkmon_id[str(i)] = (t)
    pkmon_num[t] = str(i)
for _ in range(M):
    s = input().strip()
    if s in pkmon_id:
        print(pkmon_id[s])
    else:
        print(pkmon_num[s])
