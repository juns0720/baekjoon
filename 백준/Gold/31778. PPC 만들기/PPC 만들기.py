import sys
input = sys.stdin.readline

n,k = map(int,input().split())
S = list(input().strip())


s,e = 0, n-1

while s < e and k > 0:
    if S[s] == 'C':
        if S[e] == 'P':
            S[s], S[e] = S[e], S[s]
            s += 1
            e -= 1
            k -= 1
        else:
            e -= 1
    else:
        s += 1

def cal_cost(p):
    return (p*(p-1)) // 2

cnt = 0
res = 0
for i in range(n):
    if S[i] == 'P':
        cnt += 1
    elif S[i] == 'C':
        res += cal_cost(cnt)

print(res)