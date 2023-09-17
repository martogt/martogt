# line_input = input()
#
# txt1, txt2 = line_input.split()
# str1 = []
# str2 = []
# str1 = ([ord(el) for el in txt1])
# str2 = ([ord(el) for el in txt2])
#
# result = 0
#
# if len(str1) == len(str2):
#     for idx in range(len(str1)):
#         result += str1[idx] * str2[idx]
# else:
#     if len(str1) > len(str2):
#         result += str1[-(len(str1) - len(str2))]
#         for idx in range(len(str1) - (len(str1) - len(str2))):
#             result += str1[idx] * str2[idx]
#     else:
#         result = sum(str2[:-(len(str2) - abs(len(str1) - len(str2))):])
#         for idx in range(len(str1)):
#             result += str1[idx] * str2[idx]
# print(result)


str1, str2 = input().split()

total_sum = 0

for i in range(min(len(str1), len(str2))):
    total_sum += ord(str1[i]) * ord(str2[i])

if len(str1) > len(str2):
    for i in range(len(str2), len(str1)):
        total_sum += ord(str1[i])
elif len(str2) > len(str1):
    for i in range(len(str1), len(str2)):
        total_sum += ord(str2[i])

print(total_sum)
