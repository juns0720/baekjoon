import sys
input = sys.stdin.readline
t = 0
num = int(input())
list1 = []
for i in range(num):
 list1.append(int(input()))

for z in range(num): 
    j = num-z          
    for i in range(1,j):                    
        if list1[i-1] > list1[i]:
            t = list1[i]
            list1[i] = list1[i-1]
            list1[i-1] = t

for i in range(len(list1)):
    print(list1[i])

