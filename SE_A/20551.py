T = int(input())
for j in range(T):
    eat = 0
    flag = True
    a = list(map(int,input().split()))
    for i in range(2,0,-1):
        if a[i] < i+1 or a[0] < 1:
            flag = False
            break
        if a[i] <= a[i-1]:
            eat = eat + a[i-1] - a[i] + 1
            a[i-1] = a[i-1] - eat
    if flag:
        print(f"#{j+1} {eat}")
    else:
        print(f"#{j+1} {-1}")
