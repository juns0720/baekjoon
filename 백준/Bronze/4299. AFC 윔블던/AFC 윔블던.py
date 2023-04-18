apb,amb = map(int,input().split())
a = (apb+amb)//2
b = ((apb+amb)//2-amb)
if (apb+amb) % 2 or apb - amb < 0 or apb + amb < 0:
    print(-1)
else:
    print(max(a,b),min(a,b))