n_cars = int(input())

cars = {}

for _ in range(n_cars):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = [mileage, fuel]

while True:
    line_input = input()
    if line_input == "Stop":
        break

    line_input = line_input.split(" : ")

    command = line_input[0]
    car_model = line_input[1]

    if command == "Drive":
        distance = int(line_input[2])
        car_fuel = int(line_input[3])

        if car_model in cars:
            car_mileage = int(cars[car_model][0])
            fuel_in_car = int(cars[car_model][1])

            if car_mileage < 100000 and fuel_in_car >= car_fuel:
                cars[car_model][0] += distance
                cars[car_model][1] -= car_fuel
                print(f"{car_model} driven for {distance} kilometers. {car_fuel} liters of fuel consumed.")

            if cars[car_model][0] >= 100000:
                print(f"Time to sell the {car_model}!")
                del cars[car_model]

            if fuel_in_car < car_fuel:
                print("Not enough fuel to make that ride")

    elif command == "Refuel":
        refuel = int(line_input[2])
        fuel_in_car = int(cars[car_model][1])
        total_fuel = fuel_in_car + refuel

        if total_fuel > 75:
            print(f"{car_model} refueled with {75 - cars[car_model][1]} liters")
            cars[car_model][1] = 75
        else:
            cars[car_model][1] = total_fuel
            print(f"{car_model} refueled with {refuel} liters")

    elif command == "Revert":
        revert = int(line_input[2])
        cars[car_model][0] -= revert

        if cars[car_model][0] < 10000:
            cars[car_model][0] = 10000
        else:
            print(f"{car_model} mileage decreased by {revert} kilometers")

for car in cars:
    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")
