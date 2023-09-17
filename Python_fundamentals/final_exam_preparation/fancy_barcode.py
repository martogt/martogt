import re

n_code = int(input())
product = []
group = []

for n in range(n_code):
    barcode = input()
    barcode_matches = re.findall(r"@#+[A-Z][A-Za-z\d+]+[A-Z]@#+", barcode)
    barcode_full = ", ".join(barcode_matches)

    if barcode not in barcode_matches:
        print("Invalid barcode")

    else:
        product.extend(barcode_matches)
        for el in barcode_full:
            if el.isdigit():
                group.extend(el)
        if not group:
            group.append("00")
        print(f"Product group: {''.join(group)}")
        group.clear()
