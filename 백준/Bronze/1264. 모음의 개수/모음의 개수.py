import sys
input = sys.stdin.readline

gather = ['a','e','i','o','u']
while True:
    Sum = 0
    s = input().strip().lower()
    if s == '#':
        break
    for i in gather:
        Sum+=s.count(i)
    print(Sum)
    