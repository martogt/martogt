intersect_number = int(input())

longest_interesct = set()

for _ in range(intersect_number):
    first_range, second_range = input().split("-")
    first_start, first_end = [int(el) for el in first_range.split(",")]
    second_start, second_end = [int(el) for el in second_range.split(",")]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    current_interesct = first_set & second_set

    if not longest_interesct:
        longest_interesct = current_interesct
    else:
        if len(current_interesct) > len(longest_interesct):
            longest_interesct = current_interesct

print(f"Longest intersection is {[el for el in longest_interesct]} with length {len(longest_interesct)}")
