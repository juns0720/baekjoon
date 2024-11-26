import sys
import math
sys.setrecursionlimit(10**2)
input = sys.stdin.readline


n = int(input())

def prime():
    primes = [i for i in range(n+1)]
    for i in range(2,n+1):
        for j in range(i*i,n+1,i):
            primes[j] = 0

    return primes

primes = prime()
primes[1] = 0

def odd(n):
    for num in range(n,1,-1):
        if primes[num] and primes[n-num]:
            print(2,3,n-num,num)
            exit()

def even(n):
    for num in range(n,1,-1):
        if primes[num] and primes[n-num]:
            print(2,2,n-num,num)
            exit()



if n < 8:
    print(-1)
even(n-4)
odd(n-5)

print(-1)