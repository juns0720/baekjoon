import sys
input = sys.stdin.readline




s = input().strip()
n = int(input())
key = []
for i in range(n):
    key.append(input().strip())

for i in range(n):

    for j in range(0, 26):
        tmp = []
        for k in s:
            tmp.append(chr(((ord(k)%97 + j)%26)+97))
        s2 = ''.join(tmp)
        if key[i] in s2:
            print(s2)
            exit(0)