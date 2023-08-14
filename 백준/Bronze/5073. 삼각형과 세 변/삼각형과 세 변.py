import sys
input = sys.stdin.readline
while True:
    nl = list(map(int,input().split()))
    if nl[0] == 0 and nl[1] == 0 and nl[2] == 0:
        break
    nl.sort()
    if nl[0] + nl[1] <= nl[2]:
        print("Invalid")
    elif nl[0] == nl[1] and nl[1] == nl[2]:
        print("Equilateral")
    elif nl[0] != nl[1] and nl[1] != nl[2] and nl[2] != nl[0]:
        print("Scalene")
    elif nl[0] == nl[1] or nl[1] == nl[2] or nl[2] == nl[0]:
        print("Isosceles")