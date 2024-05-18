T = int(input())
for j in range(T):
    N, K = map(int,input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    result = []
    for i in range(N - K + 1):
        for x in range(i + (K - 1), N):
            res = a[i] - a[x]
            result.append(res)
    print("#%d %d" % (j+1, min(result)))