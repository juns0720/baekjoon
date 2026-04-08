import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

cnt_a = a.count('1')
cnt_b = b.count('1')

limit = cnt_a
if cnt_a % 2 == 1:
    limit += 1

if limit >= cnt_b:
    print("VICTORY")
else:
    print("DEFEAT")