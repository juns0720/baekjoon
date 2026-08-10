def solution(n, s):
    answer = []

    for i in range(n,1,-1):
        n1 = (s+1)//i
        if n1 == 0:
            answer = [-1]
            break
        answer.append(n1)
        s -= n1
    else:
        if s == 0:
            answer = [-1]
        else:
            answer.append(s)
        
    return sorted(answer)