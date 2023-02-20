import sys
input = sys.stdin.readline
#분해합 = n = 5일때 본인+각자리수의 합. =>5+5

n = int(input())
ans = 0

for i in range(1,n):
    t = [int(j) for j in str(i)]  
    q = sum(t)+i
    if q == n:
        ans = i
        break
if ans != 0:
    print(ans)
else:
    print(0)
