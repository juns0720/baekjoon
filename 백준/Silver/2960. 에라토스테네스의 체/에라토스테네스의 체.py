import sys
import math
input = sys.stdin.readline



def make_prime():
    arr = [i for i in range(MAX)]
    cnt = 0
    for i in range(2, MAX):
        for j in range(i, MAX, i):
            if arr[j]:
                cnt+=1
                arr[j] = 0
                if cnt == K:
                    print(j)
                    exit()

N,K = map(int,input().split())
MAX = N+1
prime = make_prime()
