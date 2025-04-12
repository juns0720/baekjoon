lst = [int(input()) for _ in range(10)]
res = lst[0] - sum(lst[1:])
print(res)