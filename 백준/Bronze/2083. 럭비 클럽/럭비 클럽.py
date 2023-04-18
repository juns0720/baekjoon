import sys
input = sys.stdin.readline

while True:
    s = input().split()
    if s[0] == '#' and s[1] == '0' and s[2] == '0':
        break
    print(s[0] ,end='')
    if int(s[1]) > 17 or int(s[2]) >=80:
        print(" Senior")
    else:
        print(" Junior")