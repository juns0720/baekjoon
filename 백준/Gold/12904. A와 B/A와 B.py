import sys
input = sys.stdin.readline
S = input().strip()
T = list(input().strip())

while True:
    if len(T) == len(S):
        break
    if T[-1] == 'B':
        T.pop()
        T.reverse()       
    else:
        T.pop()
if ''.join(T) == S:
    print(1)
else:
    print(0)