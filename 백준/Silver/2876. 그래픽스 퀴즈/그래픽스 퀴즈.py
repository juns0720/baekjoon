import sys
input = sys.stdin.readline

n = int(input())

tables = [sorted(list(map(int,input().split()))) for _ in range(n)]

max_student = 0
grade = 5

for i in range(5,0,-1):
    cnt = 0
    for table in tables:
        if i in table:
            cnt += 1
        else:
            if max_student <= cnt:
                grade = i
                max_student = cnt
            cnt = 0
    if max_student <= cnt:
        grade = i
        max_student = cnt
        cnt = 0
print(max_student, grade)