import sys

input = sys.stdin.readline

word = list(input().strip())
left_stack = []
right_stack = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if word:
            right_stack.append(word.pop())
    elif command[0] == 'D':
        if right_stack:
            word.append(right_stack.pop())
    elif command[0] == 'B':
        if word:
            word.pop()
    elif command[0] == 'P':
        word.append(command[1])

word.extend(reversed(right_stack))
print(''.join(word))
