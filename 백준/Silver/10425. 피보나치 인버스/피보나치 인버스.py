import sys
input = sys.stdin.readline

fibo = [0, 1, 1, 2, 3]

N = 5
while N <= 100000:
    num = fibo[-1] + fibo[-2]
    fibo.append(num)
    N += 1

for tc in range(int(input())):
    n = int(input())
    s = 0
    e = len(fibo)  
    while s < e:  
        mid = (s + e) // 2
        if fibo[mid] < n: 
            s = mid + 1  
        else:
            e = mid  

    if s == 1: 
        s = 2
    print(s)  