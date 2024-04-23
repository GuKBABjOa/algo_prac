x = int(input())
case = list(map(int, input().split()))

# 역방향 수열 생성
reverse_case = case[::-1]

# 가장 긴 증가하는 부분 수열
increase = [1 for i in range(x)]

# 가장 긴 감소하는 부분 수열 (reversed)
decrease = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j] + 1)

for i in range(x):
    for j in range(i):
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[x - i - 1] - 1

print(max(result))
