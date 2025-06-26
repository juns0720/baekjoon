import sys
input = sys.stdin.readline

n,p,q = map(int,input().split())

dic = dict()
def recursion(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    a = n//p
    b = n//q
    if a in dic:
        ra = dic[a]
    else:
        ra = recursion(a)
        dic[a] = ra
    
    if b in dic:
        rb = dic[b]
    else:
        rb = recursion(b)
        dic[b] = rb
    
    return  ra+rb

print(recursion(n))
