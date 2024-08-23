import sys
input = sys.stdin.readline

N = int(input())

def recursion(k):
    if k == 1:
        return ['*']
    tmp = []
    ## 윗줄
    tmp.append('*'*(4*k-3))
    tmp.append('*' + ' '*(4*k-5) + '*')
    
    ## 가운데
    for s in recursion(k-1):
        tmp.append('* ' + s + ' *')

    ## 아랫 줄
    tmp.append('*' + ' '*(4*k-5) + '*')
    tmp.append('*'*(4*k-3))

    return tmp

print('\n'.join(recursion(N)))