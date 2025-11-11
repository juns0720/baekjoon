import sys
input = sys.stdin.readline

dic = {'char': 2, 'int': 8, 'long_long': 16}
s = input().strip()
n = int(input())
lst = [0]

prev = 0
for i in list(input().split()):
    lst.append(prev + dic[i])
    prev += dic[i]

res = []
for i in range(1,n+1):
    res.append(int('0x'+s[lst[i-1]:lst[i]],16))
print(*res)