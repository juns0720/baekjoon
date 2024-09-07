import sys
input = sys.stdin.readline

def checkPrime():
    for i in range(2, N+1):
        if arr[i] == 0:
            continue
        for j in range(i*2, N+1, i):
            arr[j] = 0
    for i in range(2,N+1):
        if arr[i] != 0:
            prime.append(i)

N = int(input())
if N == 1:
    print(0)
    exit()
arr = [i for i in range(N+1)]
prime = []
checkPrime()
s,e = 0,0
cur_num = prime[0]
res = 0
while s <= e:
    if cur_num < N:
        e+=1
        if e > len(prime)-1:
            break
        cur_num+=prime[e]
    elif cur_num > N:
        cur_num-=prime[s]
        s+=1
    else:
        res+=1
        cur_num-=prime[s]
        s+=1
print(res)