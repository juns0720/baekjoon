import sys
input = sys.stdin.readline

fibo = [0,1,1,2,3]
MAX = (10**21000)
num = 0
while num <= MAX:
    num = fibo[-1] + fibo[-2]
    fibo.append(num)



for tc in range(int(input())):
    n = int(input())
    s = 0
    e = len(fibo) + 1
    while s+1 < e:
        mid = (s + e) //2
        if fibo[mid] < n:
            s = mid
        else:
            e = mid
    if e == 1:
        e = 2
    print(e)
