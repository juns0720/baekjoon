import sys
input = sys.stdin.readline

n,p,q,x,y = map(int,input().split())

dic = {0:1}
def recursion(n):
    if n in dic:
        return dic[n]
    a = n//p - x
    if a < 1:
        a = dic[0]
    else:
        a = recursion(a)

    b = n//q - y
    if b < 1:
        b = dic[0]
    else:
        b = recursion(b)
    dic[n] = a + b
    return dic[n]

print(recursion(n)) 