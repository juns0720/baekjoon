import sys
from itertools import combinations
input = sys.stdin.readline



def make_prime():
    prime = [i for i in range(100001)]
    for i in range(2,100001):
        for j in range(i*2, 100001, i):
            prime[j] = 0
    prime[0], prime[1] = 0,0
    return prime

            
prime = make_prime()

while True:
    max_prime = 2
    s = input().strip()
    if s == '0':
        break
    end_point = []
    for i in range(len(s)):
        if int(s[i]) % 2 == 0:
            continue
        end_point.append(i)
    for end in end_point:
        start_idx = end - 4
        if start_idx < 0:
            start_idx = 0

        for start in range(start_idx,end+1):
            num = int(s[start:end+1])
            if prime[num]:
                max_prime = max(max_prime, num)

    print(max_prime)
  