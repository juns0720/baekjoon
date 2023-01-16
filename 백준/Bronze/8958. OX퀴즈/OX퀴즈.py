import sys
input = sys.stdin.readline

case = int(input())

for i in range(case):
    count = 0
    score = 0
    a = (input())

    for i in range(len(a)):
        if a[i] == "O":
            count+=1
            score +=count
        elif a[i] == "X":
            count = 0

        
    print(score)