nums = tuple(float(x) for x in input().split())

occurrences = {}

for num in nums:
    if num not in occurrences:
        occurrences[num] = nums.count(num)
        print(f'{num} - {nums.count(num)} times')
