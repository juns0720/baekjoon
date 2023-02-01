import sys
input = sys.stdin.readline


l1 = list(input().strip())
l2 = []

n = int(input())
  
for i in range(n):
    od = input().split()
    if od[0] =='L':
        if len(l1) > 0:
            l2.append(l1.pop())

    if od[0] =='D':
        if len(l2) > 0:
            l1.append(l2.pop())

    if od[0] =='B':
        if len(l1) > 0:
            l1.pop()

    if od[0] =='P':
        l1.append(od[1])
l2.reverse()
l1.extend(l2)

t = ''.join(l1)
print(t)