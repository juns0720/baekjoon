case = int(input())
count = 0
score = 0
list1=[]
for i in range(case):
    a = str(input())
    for i in range(len(a)):
        if a[i] == "O":
            count+=1
        elif a[i] == "X":
            count = 0
        
        score +=count
    print(score)
    score = 0
    count = 0  
