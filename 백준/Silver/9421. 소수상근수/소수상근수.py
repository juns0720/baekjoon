import sys
input = sys.stdin.readline



def make_prime():
    arr = [i for i in range(N+1)]
    for i in range(2,int(N**0.5)+1):
        for j in range(i**2,N+1,i):
            arr[j] = 0
    
    tmp = []
    for i in range(2,N+1):
        if arr[i]:
            tmp.append(i)
    return tmp


N = int(input())
primes = make_prime()


dic = {1:1}
def find(n):
    if n in dic:
        return dic[n]
    
    tmp = list(map(int,str(n)))
    ni = 0
    for i in tmp:
        ni += i**2
    dic[n] = 0
    dic[n] = find(ni)
    return dic[n]
for p in primes:
    find(p)
    if dic[p]:
        print(p)