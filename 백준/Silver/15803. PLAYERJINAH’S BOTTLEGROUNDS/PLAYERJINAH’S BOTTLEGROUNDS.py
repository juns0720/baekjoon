import sys

p = [list(map(int,input().split())) for _ in range(3)]

p.sort(key = lambda x :x[0])

ans = "WHERE IS MY CHICKEN?"

for i in range(2):
    if p[1][i] == p[0][i] and p[2][i] == p[0][i]:
        print(ans)
        exit()

for i in range(1,3):
    if p[i][0] // p[0][0] != p[i][1] // p[0][1]:
        ans = "WINNER WINNER CHICKEN DINNER!"
        break
    if p[i][0] == p[i][0]:
      if p[i][1] % p[0][1] != 0:
        ans = "WINNER WINNER CHICKEN DINNER!"
        break
    elif p[i][1] == [i][1]:
      if p[i][0] % p[0][0] != 0:
        ans = "WINNER WINNER CHICKEN DINNER!"
        break


print(ans)
