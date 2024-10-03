N,M = map(int,input().split())
house = []
for i in range(N):
    house.append(int(input()))
house.sort()



def binary_search():
    s = 1
    e = int(1e9)+1
    while s+1 < e:
        mid = (s+e)//2
        cnt = 1
        prev = house[0]
        for i in range(1,N):
            if house[i]-prev >= mid:
                cnt+=1
                prev = house[i]
        if cnt < M:
            e = mid
        else:
            s = mid
    return s
print(binary_search())


