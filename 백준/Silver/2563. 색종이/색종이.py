import sys
input = sys.stdin.readline


t = [[0 for i in range(101)] for j in range(101)]     #100x100 도화지
num = int(input())
count = 0
p = []

for i in range(num):               # 3 7     15 7   5 2
    p.append(list(map(int,input().split())))                

for z in range(num):
    for i in range(100):         
        for j in range(100):        
            if i < (p[z][1]+9) and i >= (p[z][1]-1):
                if j < (p[z][0]+9) and j >= (p[z][0]-1):
                    t[i][j] = 1






for i in range(100):        #세로   
    for j in range(100):        #가로
        if t[i][j] == 1:
            count+=1

print(count)
