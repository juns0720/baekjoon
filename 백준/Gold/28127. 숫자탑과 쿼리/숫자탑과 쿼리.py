import sys
input = sys.stdin.readline

Q = int(input())
for i in range(Q):
    a,d,x = map(int,input().split())
    Max,gap = a,a
    floor = 1
    while x > Max:
        gap = gap+d
        Max +=gap
        floor+=1
    width = gap-(Max - x)
    print(floor,width)
    
    
        

