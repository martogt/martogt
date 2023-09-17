import re

text = input()
result = []
travel_points = 0
n = 0

matches = re.findall(r'=([A-Z][a-zA-Z]{3,})=|/([A-Z][a-zA-Z]{3,})/', text)

for match in matches:
    result.append(''.join(match))
    travel_points += int(len(result[n]))
    n += 1

destination = ', '.join(result)
print(f'Destinations: {destination}')
print(f'Travel Points: {travel_points}')
