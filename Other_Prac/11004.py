import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(map(int, input().split()))
num = sorted(num)
print(num[K-1])
