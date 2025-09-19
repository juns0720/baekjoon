import sys
input = sys.stdin.readline
MOD = 1000000007
A = int(input())
X = int(input()) 

dic = {1 : A}
def rec(n):
    if n in dic:
        return dic[n]

    if n % 2 == 0:
        res = (rec(n//2)**2) % MOD
    else:
        a = rec(n//2) % MOD
        b = rec((n//2)+1) % MOD
        res = (a*b) % MOD

    dic[n] = res
    return dic[n]

print(rec(X))