import sys
input = sys.stdin.readline

c = ['c=','dz=','c-','d-','lj','nj','s=','z=']
str = input()

for i in range(len(c)):
    str = str.replace(c[i],'1')

print(len(str)-1)