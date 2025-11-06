import sys
input = sys.stdin.readline

n = int(input())

s1 = "@@@"*n + " "*n + "@"*n
s2 = "@"*n + " "*n + "@"*n + " "*n + "@"*n
s3 =  "@"*n + " "*n + "@@@"*n

for _ in range(n):
    print(s1)

for _ in range(3*n):
    print(s2)

for _ in range(n):
    print(s3)  