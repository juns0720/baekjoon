import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
students = []
is_win = 0
for i in range(N):
    is_win |= (1 << i)
res = -1


for _ in range(M):
    student = 0
    for p in list(map(int,input().split()))[1:]:
        student |= (1 << p-1)
    students.append(student)

def recursion():
    for i in range(1, M+1):
        for cur_student in combinations(students,i):
            tmp_st = 0
            for st in cur_student: 
                tmp_st |= st
            if tmp_st == is_win:
                return i
    return -1

print(recursion())
