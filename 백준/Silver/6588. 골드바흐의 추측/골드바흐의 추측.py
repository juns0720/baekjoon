import sys
input = sys.stdin.readline

arr = [0 for _ in range(1000001)]
for i in range(2,1001):
    if arr[i] == 0:
        for j in range(i+i,1000001,i):
            arr[j] = 1
while True:
    n = int(input())
    if n == 0:
        break
    flag = False
    mid = n//2
    for i in range(3,mid+1):
        if arr[i] == 0 and arr[n-i] == 0:
            print(n,'=',i,'+',n-i)
            flag = True
            break
    if flag == False:
        print("Goldbach's conjecture is wrong.")