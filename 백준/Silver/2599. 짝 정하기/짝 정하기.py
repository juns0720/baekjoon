import sys
input = sys.stdin.readline



# def cal(male,female,match):

N = int(input())
student = [list(map(int,input().split())) for _ in range(3)]
ab,ac,ba,bc,ca,cb = 0,0,0,0,0,0

for i in range(student[0][0]):
    ab = i
    ac = student[0][0]-i
    bc = student[2][1]-ac
    ba = student[1][0]-bc
    ca = student[0][1]-ba
    cb = student[2][0]-ca
    res = ab+ac+bc+ba+ca+cb
    if ab>=0 and bc>=0 and ba>=0 and bc>=0 and ca>=0 and cb>=0 and res == N:
        print(1)
        print(ab,ac)
        print(ba,bc)
        print(ca,cb)
        exit()
print(0)