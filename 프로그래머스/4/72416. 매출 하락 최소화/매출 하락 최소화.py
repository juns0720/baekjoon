def solution(sales, links):
    answer = 0
    N = len(sales)
    graph = [[] for _ in range(N)]
    INF = float('inf')

    for v1, v2 in links:
        v1 -= 1
        v2 -= 1
        graph[v1].append(v2)  # 팀장 → 팀원 방향만 저장

    dp = [[0, 0] for _ in range(N)]

    # 루트부터 방문 순서 기록
    order = []
    stack = [0]
    while stack:
        v1 = stack.pop()
        order.append(v1)
        for v2 in graph[v1]:
            stack.append(v2)

    # 역순으로 처리 → 자식(v2)이 항상 먼저 계산됨
    for v1 in reversed(order):
        dp[v1][0] = sales[v1]
        if not graph[v1]:
            continue

        include = 0
        exclude = INF
        for v2 in graph[v1]:
            include += min(dp[v2])
            exclude = min(exclude, dp[v2][0] - min(dp[v2]))

        dp[v1][0] += include
        dp[v1][1] = include + exclude

    answer = min(dp[0])
    return answer