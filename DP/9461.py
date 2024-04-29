def wave(n):
    dp = [0, 1, 1, 1, 2, 2] + [0] * (n - 5)
    for i in range(6, n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(wave(n))
