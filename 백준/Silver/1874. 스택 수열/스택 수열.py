import sys
input = sys.stdin.readline

Stack = []
Last = []                
count=1

n = int(input())
q = 1

for i in range(n):
    t = int(input())       

    while count <= t :
        Stack.append(count)
        Last.append('+')
        count+=1

    if Stack[-1] == t:
        Stack.pop()
        Last.append('-')
    else:
        q = 0
        print('NO')
        break
     

if q == 1:
    for i in Last:
        print(i)