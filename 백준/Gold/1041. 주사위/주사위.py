import sys
input = sys.stdin.readline

d = [
    [1,2,0],[1,2,5],
    [1,3,0],[1,3,5],
    [3,4,0],[3,4,5],
    [2,4,0],[2,4,5]]

n = int(input())
arr = list(map(int,input().split()))
if n == 1:
    print(sum(sorted(arr)[:5]))
    exit()

comb = []

for i,j,k in d:
    comb.append([arr[i],arr[j],arr[k]])

comb.sort(key = lambda x: sum(x))
C = sorted(comb[0])

if n == 2:
    res = (n**2)*((C[0]+C[1])*2 + C[2])
else:
    res = (n**2)*C[0]*2 + 2*(2*n*C[1] + (n-2)*n*C[0]) + C[2]*4 + 4*(n-2)*C[1] + C[0]*((n-2)**2)
    

print(res)