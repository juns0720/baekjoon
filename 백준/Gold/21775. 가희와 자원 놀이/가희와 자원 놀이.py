import sys
input = sys.stdin.readline

N,T = map(int,input().split())

turns = list(map(int,input().split()))
use = {}
users = [['','',''] for _ in range(N+1)]

i = 0
def user_init(user):
    users[user] = ['','','']

def acquire(user,id, command, card_number,flag):
    if card_number in use:
        users[user] = [id,command,card_number]
    else:
        use[card_number] = user
        if flag:
            user_init(user)
    print(id)

def release(id,card_number):
    use.pop(card_number)
    print(id)

cards = [list(input().split()) for _ in range(T)]

i = 0
turn = 0
while turn < T:
    user = turns[turn]
    if users[user][0] != '':
        acquire(user, users[user][0],users[user][1],users[user][2],1)
    else:
        card = cards[i]
        if card[1] == 'next':
            print(card[0])
        elif card[1] == 'acquire':
            acquire(user,card[0],card[1],card[2],0)
        else:
            release(card[0],card[2])
        i += 1
    turn += 1