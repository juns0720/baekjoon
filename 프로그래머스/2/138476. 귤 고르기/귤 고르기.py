def solution(k, t):
    res = dict()
    answer = 0
    for i in t:
        if i in res:
            res[i]+=1
        else:
            res[i] = 1
    res = sorted(res.items(), key = lambda x : x[1], reverse=True)

    cnt = 0
    for i in res:
        if cnt > k-1:
            break
        if cnt < k:
            answer+=1
            cnt+=i[1]
    return answer