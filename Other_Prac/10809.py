s = input()
a = [-1]*26
for i in s:
    a[ord(i)-97] = s.index(i)
for i in a:
    print(i, end=" ")
