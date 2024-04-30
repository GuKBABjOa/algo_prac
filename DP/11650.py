import sys

N = int(sys.stdin.readline())
points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.sort()

for point in points:
    sys.stdout.write(str(point[0]) + " " + str(point[1]) + "\n")
