for tc in range(int(input())):
    N = int(input())
    edges = sorted(list(map(int,input().split())))
    min_cost = sum(edges[:N-1])
    if N < 4:
        max_cost = min_cost
    else:
        max_cost = 0
        for i in range(1,N):
            idx = (i*(i-1) // 2)
            max_cost += edges[idx]

    print(min_cost, max_cost)