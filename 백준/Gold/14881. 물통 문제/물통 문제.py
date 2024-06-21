import sys
input = sys.stdin.readline

def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a



for i in range(int(input())):
    a,b,c = map(int,input().split())
    num = gcd(a,b)
    if max(a,b) < c:
        print("NO")
        continue

    if c % num == 0:
        print("YES")
    else:
        print("NO")