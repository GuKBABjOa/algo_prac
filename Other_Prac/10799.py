def cut_bar(s):
    stack = []
    total = 0
    pre = ''
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            stack.pop()
            if pre == '(':
                total += len(stack)
            else:
                total += 1
        pre = c
    return total

s = input().strip()
print(cut_bar(s))
