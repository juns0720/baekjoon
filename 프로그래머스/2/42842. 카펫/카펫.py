
def solution(brown, yellow):
    answer=[]
    tile = brown+yellow
    for width in range(tile,2,-1):
        height = tile//width
        if width*(height) == tile:
            if (width-2) * (height-2) == yellow:
                answer.append(width)
                answer.append(height)
                break
    return answer