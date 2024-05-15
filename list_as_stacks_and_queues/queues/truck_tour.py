from collections import deque

petrol_pumps = int(input())
index = 0
pumps = deque()

for i in range(petrol_pumps):
    pump = list(map(int, input().split()))
    pumps.append(pump)

total_petrol = 0
total_distance = 0
starting_point = 0

for i in range(petrol_pumps):
    petrol, distance = pumps[i]
    total_petrol += petrol
    total_petrol -= distance
    total_distance += distance

    if total_petrol < 0:
        starting_point = i + 1
        total_petrol = 0

print(starting_point)
