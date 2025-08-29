import sys
input = sys.stdin.readline

N = int(input())

dic = {1:0, 2:1}
res = 0
def recursion(n):

    if n < 3 or n in dic:
        return dic[n]

    if n % 2 == 0:
        dic[n] = (n//2)**2
        dic[n] += recursion(n//2)
        dic[n] += recursion(n//2)
    else:
        dic[n] = (n//2) * (n//2+1)
        dic[n] += recursion(n//2)
        dic[n] += recursion(n//2+1)
    return dic[n]

recursion(N)
print(dic[N])