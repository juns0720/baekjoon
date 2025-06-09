import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        if n % 6 == 0:
            print("Y")
        else:
            print("N")
    except:
        exit()