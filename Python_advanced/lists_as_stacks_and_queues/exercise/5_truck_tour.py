from collections import deque

n = int(input())

pumps = deque()
start_position = 0
stop = 0

for _ in range(n):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

while stop < n:
    fuel = 0
    for i in range(n):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stop += 1
print(start_position)
