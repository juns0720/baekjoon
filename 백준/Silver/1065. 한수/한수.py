import sys
input = sys.stdin.readline
count = 0
num = int(input())

for i in range(1,num+1):
    a = (i//100)   
    b = ((i%100)//10) 
    c =((i%100)%10)
    
    if  i >= 1 and i < 10:              #등차수열을 이룬다면
        count+=1
    elif i >= 10 and i < 100:
        count+=1
    elif i >= 100 and i < 1000:
        if b-a == c-b:
            count+=1
        

print(count)
