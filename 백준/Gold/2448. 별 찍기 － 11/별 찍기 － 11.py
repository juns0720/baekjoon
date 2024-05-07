import sys
input = sys.stdin.readline

N = int(input())


def print_star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    l = n//2
    stars = print_star(l)
    arr = []

    for i in stars:
        arr.append(" "*l + i + " "*l)
    for i in stars:
        arr.append(i + ' ' + i)

    return arr

print('\n'.join(print_star(N)))