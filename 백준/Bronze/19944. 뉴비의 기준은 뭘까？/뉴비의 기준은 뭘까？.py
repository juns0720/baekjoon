N,M = map(int,input().split())

if M < 3:
    print("NEWBIE!")
elif 2 < M < N+1:
    print("OLDBIE!")
else:
    print("TLE!")