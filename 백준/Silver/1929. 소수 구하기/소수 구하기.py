import math

def prime(n,m):
    array = [True for i in range(m+1)]
    
    for i in range(2,int(math.sqrt(m))+1):
        if array[i] == True:
            j = 2
            while i  * j <= m:
                array[i*j] = False
                j+=1
    
    for i in range(n,m+1):
        if i !=1:
            if array[i] == True:
                print(i)

N,M = map(int,input().split())
prime(N,M)
