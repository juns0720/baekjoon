import sys
input = sys.stdin.readline

def recursion(t):
    if S == t:
        print(1)
        exit()

    if len(t) == 0:
        return

    if t[-1] == 'A':
        recursion(t[:-1])
    if t[0] == 'B':
        recursion(t[1:][::-1])


S = input().strip()
T = input().strip()
recursion(T)
print(0)
