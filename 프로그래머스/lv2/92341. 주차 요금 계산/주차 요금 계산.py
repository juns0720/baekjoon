from collections import deque
import math
def solution(fees, records):
    record = []
    car_num = set()
    parking_fees = dict()
    answer = []
    # 입출차 정보 개수

    for i in range(len(records)):
        temp = records[i].split()
        car_num.add(temp[1])
        # 시간 분단위로 변환
        time = 0
        for index in range(2):
            if index == 0:
                time += int(temp[0].split(':')[index]) * 60
            else:
                time += int(temp[0].split(':')[index])
        temp[0] = time
        record.append(temp)
    record.sort(key=lambda x: int(x[1]))

    for car in sorted(car_num):
        parking_fees[car] = 0

    for i in range(len(record)):
        if record[i][2] == 'IN':
            if i == len(record) - 1:
                parking_fees[record[i][1]] += 1439 - record[i][0]
            elif record[i][1] == record[i+1][1]:
                parking_fees[record[i][1]] += record[i+1][0] - record[i][0]
            else:
                parking_fees[record[i][1]] += 1439 - record[i][0]

    for items in parking_fees.values():
        if items > fees[0]:
            answer.append(int(fees[1]+(math.ceil((items-fees[0])/fees[2]) * fees[3])))
        else:
            answer.append(fees[1])
    return answer