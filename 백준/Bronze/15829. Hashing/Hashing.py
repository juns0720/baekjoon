import sys
input = sys.stdin.readline

L = int(input())
s = list(input().strip())
c_s = []
M = 1234567891
for index in s:
    c_s.append(ord(index)-96)
i = 0
Hash = 0
for apb in c_s:
    Hash+=apb*(31**i)
    i+=1
print(Hash%M)
