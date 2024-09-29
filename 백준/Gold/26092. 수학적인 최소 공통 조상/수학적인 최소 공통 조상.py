import sys
import math
input = sys.stdin.readline
'''
메모리 제한 : 1024MB = 2^10(10^3) * 10^6Byte = 10^9Byte
배열 크기 : 10^6 * 4Byte(int)
'''

a,b = map(int,input().split())

def find_parent(num):
   tmp = {1,num}
   while num > 1:
      prime = 1
      for i in range(2,int(math.sqrt(num))+1):
         if num % i == 0:
            num //= i
            tmp.add(num)
            prime = 0
            break
      if prime:
         break
   return tmp

parentA = find_parent(a)
parentB = find_parent(b)
intersection = parentA & parentB
print(max(intersection))
