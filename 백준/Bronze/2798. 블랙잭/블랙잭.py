import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
nl = list(map(int,input().split()))
t = 0
for i in range(n[0]):          # 0 1 2 3 4 
    if i< n[0]-2:
        for j in range(i+1,n[0]):
            if j < n[0]:
                for q in range(j+1,n[0]):
                    if q < n[0]:
                        sum = nl[i]+nl[j]+nl[q]
                        if sum <= n[1] and sum >= t:
                            t = sum          
print(t)