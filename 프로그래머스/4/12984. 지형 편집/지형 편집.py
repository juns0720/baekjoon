def solution(land, P, Q):
    heights = sorted(h for row in land for h in row)
    n = len(heights)
    total = sum(heights)

    # prefix[i] = 앞에서 i개의 합
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + heights[i]
    
    answer = float('inf')
    for i in range(n):
        h = heights[i]

        build = h * i - prefix[i]
        remove = (total - prefix[i + 1]) - h * (n - i - 1)

        answer = min(answer, build * P + remove * Q)

    return answer