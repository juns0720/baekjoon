import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

player = [0 for i in range(N+1)]
for i in range(M):
    al = list(input().split())
    for j in range(len(al)):
        if int(j) % 2 == 0:
            player[int(al[j])] = max(player[int(al[j])],float(al[int(j+1)]) )
player.sort(reverse=True)
print(round(sum(player[:K]),1))


