import sys
input = sys.stdin.readline

gather = ['a','e','i','o','u']
word = ['ee','oo']
while True:
    str1 = input().strip()
    if str1 == 'end':
        break
    flag = False
    tmp = str1[0]
    tmp_s = str1[0]
    cnt = [0,0]
    for i in range(len(str1)):
        if str1[i] in gather:   #1번
            flag = True
            cnt[0]+=1
            cnt[1] = 0
        else:
            cnt[1]+=1
            cnt[0] = 0
        if cnt[0] > 2 or cnt[1] > 2:  #2번
            flag = False
            break
        if i > 0:
            if str1[i] == tmp:
                tmp_s+=str1[i]
            else:
                tmp = str1[i]
                tmp_s = str1[i]
        if len(tmp_s) > 1:  #3번
            if tmp_s in word:
                tmp_s = ''
            else:
                flag = False
                break
    if flag == True:
        print('<'+str1+'>',"is acceptable.")
    else:
        print('<'+str1+'>',"is not acceptable.")