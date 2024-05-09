import sys
input = sys.stdin.readline

N,M = map(int,input().split())


truth = set(list(input().split())[1:])
parties = [set(list(input().split())[1:]) for _ in range(M)]

for _ in range(M):
    for party in parties:
        # 해당 파티에 진실을 아는 사람이 존재하면(intersections = 교집합)
        # 해당 파티의 사람들을 진실을 아는 사람 집합에 union(합집합) 시킨다.
        if party.intersection(truth):
            truth = truth.union(party)

cnt = 0
for party in parties:
    if party & truth:
        continue
    cnt+=1
print(cnt)