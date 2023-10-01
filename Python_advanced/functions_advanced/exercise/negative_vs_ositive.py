def neg_pos(*args):
    result_neg = 0
    result_pos = 0
    stronger_num = ""
    weaker_num = ""

    for num in args[0]:
        if num < 0:
            result_neg -= num
        elif num >= 0:
            result_pos += num

    if result_pos > result_neg:
        stronger_num = "positives"
        weaker_num = "negatives"
    else:
        stronger_num = "negatives"
        weaker_num = "positives"

    return print(f"{-abs(result_neg)}\n{result_pos}\nThe {stronger_num} are stronger than the {weaker_num}")


numbers = [int(x) for x in input().split()]
neg_pos(numbers)
