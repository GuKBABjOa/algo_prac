import sys
from collections import deque

def check_cycle(student):
    team_members = dict()
    team_members[student] = 0
    queue = deque([(student, 0)])
    visited[student] = True

    while queue:
        current_student, idx = queue.popleft()
        next_student = student_choice[current_student]
        if next_student in team_members:
            return len(team_members) - team_members[next_student]
        if not visited[next_student]:
            team_members[next_student] = idx + 1
            queue.append((next_student, idx + 1))
            visited[next_student] = True
    return 0

T = int(sys.stdin.readline())
for tc in range(T):
    N = int(sys.stdin.readline())
    student_choice = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (N + 1)
    no_team = N

    for i in range(1, N + 1):
        if not visited[i]:
            no_team -= check_cycle(i)

    print(no_team)
