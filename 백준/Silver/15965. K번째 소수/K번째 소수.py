import sys
input = sys.stdin.readline

MAX = int(1e7)

def make_prime():
    arr = [i for i in range(MAX)]
    arr[1] = 0
    for i in range(2, MAX):
        for j in range(i*2, MAX, i):
            arr[j] = 0
    primes = []
    for prime in arr:
        if prime:
            primes.append(prime)
    return primes

N = int(input())

prime = make_prime()
print(prime[N-1])
