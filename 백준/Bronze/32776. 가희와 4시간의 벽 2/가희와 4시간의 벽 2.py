import sys
input = sys.stdin.readline

sab = int(input())

ma, fab, mb = map(int,input().split())

if sab <= ma + fab + mb or sab <= 240:
    print("high speed rail")
    
else:
    print("flight")