li = [0 for _ in range(10)]
for _ in range(5):
    a = int(input())
    if li[a] == 0:
        li[a]+=1
    else:
        li[a]-=1
print(li.index(1))