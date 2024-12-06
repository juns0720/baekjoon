import sys
from itertools import permutations
input = sys.stdin.readline

lst = [input().strip() for _ in range(6)]

def make_dic():
    dic = dict()
    for i in lst:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic





for i in (permutations([j for j in range(6)],3)):
    puzzle = []
    for j in i:
        puzzle.append(list(lst[j]))
    
    dic = make_dic()
    
    for row in range(3):
        word = ''.join(puzzle[row])
        if word not in dic:
            break
        dic[word]-=1
    for col in range(3):
        word = puzzle[0][col] + puzzle[1][col] + puzzle[2][col]
        if word not in dic:
            break
        dic[word]-=1
    find = 1
    for i in dic.values():
        if i != 0:
            find = 0
            break
    if find:
        for i in puzzle:
            print(''.join(i))
        exit()

print(0)