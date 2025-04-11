import sys
input = sys.stdin.readline


res = ["Not a pangram", "Pangram!", "Double pangram!!", "Triple pangram!!!"]
for tc in range(1,int(input()) + 1):
    apb = [0 for _ in range(128)]
    dic = dict()
    stc = list(input().strip().replace(' ',''))
    for s in stc:
        s = ord(s.lower())
        if 97 <= s <= 122:
            apb[s] += 1
    ans = set()
    for i in range(97,123):
        if apb[i] == 3:
            ans.add(3)
        elif apb[i] == 2:
            ans.add(2)
        elif apb[i] == 1:
            ans.add(1)
        elif apb[i] == 0:
            ans.add(0)
    ans = sorted(list(ans))
    print(f'Case {tc}: {res[ans[0]]}')