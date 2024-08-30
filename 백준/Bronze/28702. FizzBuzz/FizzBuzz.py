import sys
input = sys.stdin.readline

arr = ["Fizz", "Buzz", "FizzBuzz"]
cnt = 3
s = [input().strip() for _ in range(3)]

for s1 in s:
    if s1 not in arr:
        s1 = int(s1)
        s1+=cnt
        break
    cnt-=1
if s1 % 3 == 0 and s1 % 5 == 0:
    print("FizzBuzz")
elif s1 % 3 == 0:
    print("Fizz")
elif s1 % 5 == 0:
    print("Buzz")
else:
    print(s1)