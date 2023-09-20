from collections import deque

sequences_one = deque(set(int(x) for x in input().split()))
sequences_two = deque(set(int(x) for x in input().split()))

n = int(input())

for i in range(n):
    command = input().split()
