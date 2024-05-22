T = int(input())
for i in range(0,T):
    flag = True
    s = list(input())
    if s == s[::-1]:
        j = 0
        k = int((len(s)-1)/2)-1
        if len(s) == 3:
            if s[0] != s[2]:
                print(f"#{i+1} NO")
            else:
                print(f"#{i+1} YES")
            continue
        while(j<k):
            if s[j] != s[k]:
                flag = False
                break
            j += 1
            k -= 1
        j = int((len(s)/2)+1)
        k = len(s) - 1
        while(j<k):
            if (s[j] != s[k]) or (not flag):
                flag = False
                break
            j += 1
            k -= 1
        if flag:
            print(f"#{i+1} YES")
        else:
            print(f"#{i+1} NO")