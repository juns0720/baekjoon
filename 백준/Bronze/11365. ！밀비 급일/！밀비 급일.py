import sys
input = sys.stdin.readline

al = []

while True:
    s = input().strip()
    if s == "END":
        break
    else:
       print( ''.join(reversed(s)))
    