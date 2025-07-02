import sys
input = sys.stdin.readline

n = int(input())
side = "*"*n
mid = "*" + " "*(n-2) + "*"

print(side + " "*(2*(n-1)-1) + side)
t = n-2
for i in range(1,n-1):
    print(" "*i + mid + " "*(2*t-1) + mid)
    t -=1

print(" "*(n-1) + mid + " "*(n-2) + "*")

t = 1
for i in range(n-2,0,-1):
    print(" "*i + mid + " "*(2*t-1) + mid)
    t+=1
    
print(side + " "*(2*(n-1)-1) + side)