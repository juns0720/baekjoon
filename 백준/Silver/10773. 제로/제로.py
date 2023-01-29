import sys
input = sys.stdin.readline
Stack = []
k =int(input())

for i in range(k):
    a = int(input())
    if a == 0:           
            del Stack[-1]
    else:
        Stack.append(a)
print(sum(Stack))



