import sys
input = sys.stdin.readline

T = int(input())
numbers = list(map(int,input().split()))

for num in numbers:
   res = 0
   for i in range(1, num):
      if num % i == 0:
         res += i
   if res < num:
      print("Deficient")
   elif res == num:
      print("Perfect")
   else:
      print("Abundant")