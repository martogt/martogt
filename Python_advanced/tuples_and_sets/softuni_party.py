n = int(input())

reservation = set()

for _ in range(n):
    reservation_number = input()
    reservation.add(reservation_number)

guests = input()
while guests != 'END':

    if guests in reservation:
        reservation.remove(guests)

    guests = input()

print(len(reservation))

for names in sorted(reservation):
    print(names)
