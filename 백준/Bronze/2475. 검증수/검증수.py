s = list(map(int,input().split()))
Sum = 0

for i in s:
    Sum+=i**2
print(Sum%10)