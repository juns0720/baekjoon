import sys
input = sys.stdin.readline

n,m = map(int,input().split())

n = list(str(n))
m = list(str(m))
n.reverse()
m.reverse()
n = int(''.join(n))
m = int(''.join(m))
print(max(n,m))

