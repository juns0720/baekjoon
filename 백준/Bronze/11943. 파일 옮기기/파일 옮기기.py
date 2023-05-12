import sys
input = sys.stdin.readline

A,B = map(int,input().split())
C,D = map(int,input().split())

print(B+C if A+D > B+C else A+D)
    
    

