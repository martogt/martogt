# import re
#
# text = input()
# match = {}
#
# for let in range(len(text)):
#     matches = re.findall(text[let], text)
#     letter = matches[0]
#     match[letter] = len(matches)
#
# for let, occ in match.items():
#     print(f"{''.join(let)}: {occ} time/s")

text = tuple(input())

unic_let = sorted(set(text))

for char in unic_let:
    print(f'{char}: {text.count(char)} time/s')
