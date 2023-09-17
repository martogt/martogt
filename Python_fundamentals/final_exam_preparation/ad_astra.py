import math
import re

text = input()

need_food = 0
total_calorie = 0

pattern = r"#([a-zA-Z]+\s?[a-zA-Z]+)#(\d{2}/\d{2}/\d{2})#(\d+)#|\|([a-zA-Z]+)\|(\d{2}/\d{2}/\d{2})\|(\d+)\|"
matches = re.findall(pattern, text)

cleaned_data = [tuple(filter(lambda x: x != '', data)) for data in matches if any(x != '' for x in data)]

if not matches:
    print("You have food to last you for: 0 days!")
    exit()

for cal in cleaned_data:
    calories = int(cal[2])
    total_calorie += calories
    need_food = math.floor(total_calorie / 2000)

print(f"You have food to last you for: {need_food} days!")

for items in cleaned_data:
    food = items[0]
    date = items[1]
    calories = int(items[2])

    print(f"Item: {food}, Best before: {date}, Nutrition: {calories}")
