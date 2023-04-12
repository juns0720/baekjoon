s = input()
apb = list(range(97,123))   #a-z
for i in apb:
    print(s.find(chr(i)),end=' ')