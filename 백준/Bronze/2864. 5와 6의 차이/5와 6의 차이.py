import sys
input = sys.stdin.readline

a,b = input().strip().split()
a,b = list(a), list(b)

for i in range(len(a)):
    if a[i] == '6':
        a[i] = '5'

for i in range(len(b)):
    if b[i] == '6':
        b[i] = '5'
print(int(''.join(a)) + int(''.join(b)), end = ' ')

for i in range(len(a)):
    if a[i] == '5':
        a[i] = '6'

for i in range(len(b)):
    if b[i] == '5':
        b[i] = '6'
print(int(''.join(a)) + int(''.join(b)))