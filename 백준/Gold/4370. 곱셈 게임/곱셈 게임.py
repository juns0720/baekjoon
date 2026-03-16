import sys
input = sys.stdin.readline

winner = { 2: 'Donghyuk wins.', 9: 'Baekjoon wins.'}

while True:
    try:
        n = int(input())
    except: 
        exit()

    p = 1
    end = 0

    while not end:

        for i in [9,2]:
            p *= i

            if p >= n:
                print(winner[i])
                end = 1
                break