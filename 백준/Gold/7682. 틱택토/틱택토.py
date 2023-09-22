import sys
from itertools import permutations
input = sys.stdin.readline

while True:
    al = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    s = input().strip()
    if s == 'end':
        break
    else:
        flag = False
        flag1 = False
        x_list = []
        o_list = []
        for i in range(len(s)):
            if s[i] == 'X':
                x_list.append(i+1)
            elif s[i] == 'O':
                o_list.append(i+1)
        X,O = len(x_list),len(o_list)


        if -1 < X-O < 2:
            if X < 3 and O < 3:
                print('invalid')
                continue
            if X+O == 9 and X-O == 1:
                flag = True
            for i in permutations(x_list,3):
                if i in al and (X+O) % 2 == 1:
                    flag = True
                    flag1 = True
                    break
            for i in permutations(o_list,3):
                if i in al:
                    if O == X and not flag1 and (X+O) % 2 == 0:
                        flag = True
                    else:
                        flag = False
                    break
    if flag:
        print('valid')
    else:
        print('invalid')
