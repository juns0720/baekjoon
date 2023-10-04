a,b = [],[]
for i in range(6):
    n = int(input())
    if i < 4:
        a.append(n)
    else:
        b.append(n)
print(sum(sorted(a)[1:])+max(b))