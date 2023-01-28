import sys
input = sys.stdin.readline

n = int(input())
l = (list(map(str,str(n))))

l.sort(reverse = True)

nl = "".join(l)
print(nl)