import sys
input = sys.stdin.readline

N = int(input())
alb = {0 : 'A',1 : 'B',2 : 'C',3 : 'D',4 : 'E',5 : 'F',6 : 'G',7 : 'H'}
codes = [
    '000000',
    '001111',
    '010011',
    '011100',
    '100110',
    '101001',
    '110101',
    '111010']
key = input().strip()

idx = 0
res = ''
for i in range(N):
    cur_code = key[i*6:(i+1)*6]
    flag = 0
    tmp = []
    for code_idx in range(len(codes)):
        cnt = 0
        for j in range(6):
            if cur_code[j] != codes[code_idx][j]:
                cnt+=1
        tmp.append(cnt)
    for k in range(8):
        if tmp[k] < 2:
            res+=alb[k]
            flag = 1
            break
    if not flag:
        print(i+1)
        exit()


print(res)