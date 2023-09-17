# Input country names and capital cities
countries = input().split(", ")
capitals = input().split(", ")

# Create a dictionary using a dictionary comprehension
country_capital_dict = {country: capital for country, capital in zip(countries, capitals)}

# Print each country and its capital in the desired format
for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")
