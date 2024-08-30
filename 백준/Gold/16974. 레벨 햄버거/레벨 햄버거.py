import sys
input = sys.stdin.readline
N,X = map(int,input().split())

amount, patty = 1, 1
for i in range(N):
    amount = amount*2+3
    patty = patty*2+1

def recursion(total_amount, total_patty,res):
    global X
    if X == 0:
        print(res)
        exit()
    if X == total_amount:
        print(res+total_patty)
        exit()
    elif X < total_amount:
        if X == total_amount//2 + 1:
            print(res + total_patty//2 + 1)
            exit()
        if X > total_amount//2 + 1:
            res+= (total_patty//2 + 1)
            X -= (total_amount//2 + 1)
            recursion(total_amount//2-1, total_patty//2,res)
        else:
            X-=1
            recursion(total_amount//2-1, total_patty//2,res)

recursion(amount,patty,0)
