targets = {}

while True:
    command = input()

    if command == "Sail":
        command = input()
    if "Plunder" in command:
        plunder, town, people, gold = command.split("=>")
        if town in targets:
            if targets[town][0] == 0 or targets[town][1] == 0:
                targets.pop(town)
                print(f"{town} has been wiped off the map!")
            else:
                targets[town][0] -= int(people)
                targets[town][1] -= int(gold)
                print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        command = input()
    if "Prosper" in command:
        prosper, town, gold = command.split("=>")
        if town in targets:
            if int(gold) < 0:
                print("Gold added cannot be a negative number!")
            else:
                targets[town][1] += int(gold)
                print(f"{gold} gold added to the city treasury. {town} now has {targets[town][1]} gold.")

    if command == "End":
        break

    if len(command.split("||")) == 3:
        city, people, gold = command.split("||")

        if city in targets:
            targets[city][0] += int(people)
            targets[city][1] += int(gold)
        else:
            targets[city] = [int(people), int(gold)]

if targets:
    print(f"Ahoy, Captain! There are {len(targets.items())} wealthy settlements to go to:")
    for city in targets:
        print(f"{city} -> Population: {targets[city][0]} citizens, Gold: {targets[city][1]} kg")
