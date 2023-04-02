import sys
input = sys.stdin.readline

N,K = map(int,input().split())

man = list(map(int,input().split()))
team = []
Sum = 0
for i in range(1,N):
    team.append(man[i]-man[i-1])
team.sort()
for i in range(N-K):
    Sum+=team[i]
print(Sum)
