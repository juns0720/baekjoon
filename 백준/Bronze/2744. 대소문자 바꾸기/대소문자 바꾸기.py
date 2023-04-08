import string
s = list(input())


for i in range(len(s)):
    if s[i].isupper() == True:
        s[i] = s[i].lower()
    else:
        s[i] =s[i].upper()
print(''.join(s))