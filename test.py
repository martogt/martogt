initial_fuel = list(map(int, input().split()))
consumption_indexes = list(map(int, input().split()))
needed_fuel = list(map(int, input().split()))

altitudes_reached = []

for altitude in range(1, len(needed_fuel) + 1):
    if not initial_fuel:
        break

    current_fuel = initial_fuel[-1]
    consumption_index = consumption_indexes[0]
    required_fuel = needed_fuel[0]

    if current_fuel - consumption_index >= required_fuel:
        altitudes_reached.append(altitude)
        initial_fuel.pop()
        consumption_indexes.pop(0)
        needed_fuel.pop(0)
    else:
        break

for altitude in altitudes_reached:
    print(f"John has reached: Altitude {altitude}")

if altitudes_reached:
    if not needed_fuel:
        print("John has reached all the altitudes and managed to reach the top!")
    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        print("John failed to reach the top.")
        print("Reached altitudes: Altitude " + ", Altitude ".join(map(str, altitudes_reached)))

else:
    print("John did not reach any altitude.")
    print("John failed to reach the top.")
