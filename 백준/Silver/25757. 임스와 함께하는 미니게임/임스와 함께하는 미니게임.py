import sys
input = sys.stdin.readline

div = {'Y': 1, 'F': 2, 'O': 3}

N,game = input().split()
N = int(N)
player = set()
for i in range(N):
    player.add(input().strip())

print(len(player) // div[game])