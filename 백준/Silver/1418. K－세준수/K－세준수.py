import sys
input = sys.stdin.readline

N = int(input())
K = int(input())


def make_prime(n):
    arr = [i for i in range(n+1)]

    for i in range(2,int((n**0.5))+1):
        for j in range(i*i,n+1,i):
            if not arr[i]:
                continue
            arr[j] = 0
    primes = []
    for prime in arr:
        if prime and prime > K:
            primes.append(prime)

    return primes


primes = make_prime(N)

res = [1 for _ in range(N+1)]

for i in primes:
    for j in range(i, N+1, i):
        res[j] = 0
        
print(sum(res[1:]))
