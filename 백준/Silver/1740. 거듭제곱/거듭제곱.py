import sys
input = sys.stdin.readline

n = int(input())
binary = list(map(int,str(bin(n))[2:]))[::-1]
res = 0
for i in range(len(binary)):
    if binary[i] == 1:
        res += 3**i
print(res)