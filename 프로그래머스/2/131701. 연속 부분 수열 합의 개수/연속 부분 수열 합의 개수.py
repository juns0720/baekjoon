def solution(elements):
    e = elements*2
    res = []
    n = len(elements)
    for i in range(n):
        for j in range(1,n+1):
            res.append(sum(e[i:i+j]))
    return len(set(res))