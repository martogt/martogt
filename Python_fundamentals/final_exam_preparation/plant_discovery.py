n = int(input())

plant_library = {}

for _ in range(n):
    plant, rarity = input().split("<->")

    if plant not in plant_library:
        plant_library[plant] = [[int(rarity)], []]
    else:
        plant_library[plant][0].append(int(rarity))

while True:
    line_input = input()
    if line_input == "Exhibition":
        break

    command = line_input.split(": ")
    rate_com = command[0]
    plant_rating = command[1].split(" - ")
    plants = plant_rating[0]

    if rate_com == "Rate":
        rating = plant_rating[1]
        if plants in plant_library:
            plant_library[plants][1].append(int(rating))
        else:
            print("error")
            continue

    elif rate_com == "Update":
        new_rarity = plant_rating[1]
        if plants in plant_library:
            plant_library[plants][0] = [float(new_rarity)]
        else:
            print("error")
            continue

    elif rate_com == "Reset":
        if plants in plant_library:
            plant_library[plants][1] = [0.00]
        else:
            print("error")
            continue

print("Plants for the exhibition:")

for pl in plant_library:
    print(
        f"- {pl}; Rarity: {int(*plant_library[pl][0])}; Rating: {(sum(plant_library[pl][1]) / len(plant_library[pl][1])):.2f}")
