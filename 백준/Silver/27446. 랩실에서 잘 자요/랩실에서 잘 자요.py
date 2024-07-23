N,M = map(int,input().split())

lst = set(list(map(int,input().split())))

pages = []
for i in range(1,N+1):
    if i not in lst:
        pages.append(i)

before,res = 0,0
for cur_page in pages:
    if before:
        res+=min(7,(cur_page-before)*2)
    else:
        res+=7
    before = cur_page
print(res)
