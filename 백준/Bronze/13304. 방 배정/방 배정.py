import sys
input = sys.stdin.readline

N,K = map(int,input().split())

student = [[0,0] for _ in range(7)]
for i in range(N):
    gen, grade = map(int,input().split())
    student[grade][gen]+=1
res = []
def count_room(num):
    return (num//K)+1 if num % K != 0 else num//K

#1,2학년 계산
res.append(count_room(sum(student[1]) + sum(student[2])))
#3~6학년 계산
for i in range(2,4):
    res.append(count_room(student[i*2-1][0] + student[i*2][0]))
    res.append(count_room(student[i*2-1][1] + student[i*2][1]))

print(sum(res))