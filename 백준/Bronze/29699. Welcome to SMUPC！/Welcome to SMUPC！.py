import sys
input = sys.stdin.readline

s1 = list('WelcomeToSMUPC')
N = int(input().strip())

print(s1[N%len(s1)-1])