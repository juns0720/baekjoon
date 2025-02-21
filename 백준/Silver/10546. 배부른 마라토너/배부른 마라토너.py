import sys
input = sys.stdin.readline

N = int(input())

players = {}

for _ in range(N):
    player = input().strip()
    if player not in players:
        players[player] = 1
    else:
        players[player] += 1
for i in range(N-1):
    players[input().strip()] -= 1

for i in players.items():
    if i[1] > 0:
        print(i[0])
        break

