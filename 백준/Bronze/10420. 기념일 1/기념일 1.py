import sys

input = sys.stdin.readline

'''
1. 평년 365일
2. 윤년 366일

1. 년단위보다 작으면 month
'''
N = int(input())
year = 2014
month = 4
day = 1 + N
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
last_day = 0
while True:
    if day-days[month] < 1:
        break
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        day-=1
    day-=days[month]
    month+=1

    if month == 13:
        year+=1
        month = 1

year,month,day = str(year), str(month), str(day)
month = month.zfill(2)
day = day.zfill(2)

res = year+month+day
print(year+'-' + month + '-' + day)