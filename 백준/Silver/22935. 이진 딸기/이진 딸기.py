import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())

    if n > 15:
        if n % 14 == 1:
            if (n // 14) % 2 == 0:
                n = 1
            else:
                n = 15
        elif n % 14 == 0:
            if (n // 14) % 2 == 0:
                n = 2
            else:
                n = 14
        else:
            if (n // 14) % 2 == 0:
                n %= 14 
            else:
                n = 16 - (n % 14)
                
    binary = bin(n)[2:]
    res = ['V']*4
    idx = 3
    for i in range(len(binary)-1,-1,-1):
        if binary[i] == '1':
            res[idx] = "딸기"
        idx -= 1
    
    print(''.join(res))
