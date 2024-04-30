import sys

N = int(sys.stdin.readline())
points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((y, x))

points.sort()

for point in points:
    sys.stdout.write(str(point[1]) + " " + str(point[0]) + "\n")
