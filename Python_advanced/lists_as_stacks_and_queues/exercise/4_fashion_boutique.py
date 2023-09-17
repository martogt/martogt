clothes = ([int(x) for x in input().split()])
rack_capacity = int(input())
clothes_counter = 0
rack_counter = 0

while clothes:
    if (clothes_counter + clothes[-1]) <= rack_capacity:
        clothes_counter += clothes.pop()
        if not clothes:
            rack_counter += 1
    else:
        rack_counter += 1
        clothes_counter = 0

print(rack_counter)
