a,b = map(int,input().split())
if a < 2:
    print(0)
else:
    if a//2 <= b:
        print(a//2)
    else:
        print(b)