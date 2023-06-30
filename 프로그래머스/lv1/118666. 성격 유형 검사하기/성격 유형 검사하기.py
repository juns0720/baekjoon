def solution(survey, choices):
    character = {'R': 0,'T': 0,'C': 0,'F': 0,'J': 0,'M': 0,'A': 0,'N': 0}
    answer = ''
    for i in range(len(choices)):
        left = survey[i][0]
        right = survey[i][1]
        if choices[i] < 4:
            character[left] += (4 - choices[i])
        elif choices[i] == 4:
            continue
        else:
            character[right] += (choices[i] - 4)
    
    answer += 'T' if character['R'] < character['T'] else 'R'
    answer += 'F' if character['C'] < character['F'] else 'C'
    answer += 'M' if character['J'] < character['M'] else 'J'
    answer += 'N' if character['A'] < character['N'] else 'A'
    return answer
