A, P = map(int, input().split())
nums = [A]

while True:
    temp = str(A)
    num = 0
    for i in temp:
        num += int(i) ** P
    if num in nums:
        nums = nums[:nums.index(num)]
        break
    else:
        nums.append(num)
        A = num

print(len(nums))
