import sys
input = sys.stdin.readline
N = int(input())
paturn = list(input().strip())

for i in range(1,N):
    file = list(input().strip())
    for i in range(len(file)):
        if paturn[i] != file[i]:
            paturn[i] = '?'
print(''.join(paturn))