def even_odd(*args):
    command = args[-1]
    result = []

    if command == "even":
        for num in args[:-1]:
            if num % 2 == 0:
                result.append(num)
    elif command == "odd":
        for num in args[:-1]:
            if num % 2 != 0:
                result.append(num)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
