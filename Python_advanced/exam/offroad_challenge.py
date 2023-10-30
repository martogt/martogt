from collections import deque

fuel = deque(int(f) for f in input().split())
consumption_indexes = deque(int(c) for c in input().split())
quantities = deque(int(s) for s in input().split())

reached_altitude = {}

for i in range(len(fuel)):
    result = fuel[-1] - consumption_indexes[0]
    if result >= quantities[0]:
        fuel.pop()
        consumption_indexes.popleft()
        quantities.popleft()

        if not reached_altitude:
            reached_altitude["Altitude"] = []

        reached_altitude["Altitude"].append(i + 1)
        print(f"John has reached: Altitude {i + 1}")

    if result <= 0:
        print(f"John did not reach: Altitude {i + 1}")
        print(f"John failed to reach the top.")
        break

if not consumption_indexes and not quantities:
    print("John has reached all the altitudes and managed to reach the top!")

else:
    for key, values in reached_altitude.items():
        values_str = ', '.join([f"{key} {str(value)}" for value in values])
        result = f"Reached altitudes: {values_str}"

        print(result)
