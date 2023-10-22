# from collections import defaultdict
#
#
# def accommodate_new_pets(capacity, weight_limit, *args):
#     accommodated_animals = defaultdict(list)
#     hotel_capacity = int(capacity)
#     pet_info = args
#     pet_counter = 0
#
#     for el in pet_info:
#         pet_weight = el[1]
#         pet_type = el[0]
#
#         if pet_counter >= hotel_capacity:
#             break
#         if pet_weight <= weight_limit:
#             if pet_type not in accommodated_animals:
#                 accommodated_animals[pet_type] = []
#             accommodated_animals[pet_type].append(pet_weight)
#             pet_counter += 1
#         else:
#             continue
#
#     if pet_counter <= len(args):
#         result = f"All pets are accommodated! Available capacity: {hotel_capacity - pet_counter}.\n"
#         result += "Accommodated pets:\n"
#         for animal in sorted(accommodated_animals):
#             result += f"{animal}: {len(accommodated_animals[animal])}\n"
#     else:
#         result = "You did not manage to accommodate all pets!\n"
#         result += "Accommodated pets:\n"
#         for animal in sorted(accommodated_animals):
#             result += f"{animal}: {len(accommodated_animals[animal])}\n"
#
#     return result

def accommodate_new_pets(capacity, max_weight, *pets_data):
    accommodated_pets = {}
    result = []

    for pet_type, pet_weight in pets_data:
        if capacity <= 0:
            result.append('You did not manage to accommodate all pets!')
            break
        if pet_weight > max_weight:
            continue
        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        capacity -= 1
    else:
        result.append(f'All pets are accommodated! Available capacity: {capacity}.')

    result.append('Accommodated pets:')
    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(accommodated_pets.items())]
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
