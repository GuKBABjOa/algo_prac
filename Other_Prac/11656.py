S = input()
arr = [S[i:] for i in range(len(S))]
arr.sort()
for j in arr:
    print(j)
