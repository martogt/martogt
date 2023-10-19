from collections import deque

expression = input()

expression_deque = deque()

for index in range(len(expression)):
    if expression[index] == "(":
        expression_deque.append(index)
    elif expression[index] == ")":
        if expression_deque:
            start_index = expression_deque.pop()
            end_index = index
            print(expression[start_index:end_index + 1])
