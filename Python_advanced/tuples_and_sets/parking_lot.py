n = int(input())
parking = set()

for _ in range(n):
    direction, car = input().split(', ')

    if direction == 'IN':
        parking.add(car)
    elif direction == 'OUT':
        parking.remove(car)

if parking:
    for cars in parking:
        print(cars)
else:
    print('Parking Lot is Empty')
