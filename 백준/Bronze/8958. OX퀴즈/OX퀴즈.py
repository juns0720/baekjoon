case = int(input())

list1=[]
for i in range(case):
    count = 0
    score = 0
    a = str(input())
    for i in range(len(a)):
        if a[i] == "O":
            count+=1
        elif a[i] == "X":
            count = 0
        
        score +=count
    print(score)

