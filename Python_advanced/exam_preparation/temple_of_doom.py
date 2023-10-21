from collections import deque

tools = deque(int(t) for t in input().split())
substances = deque(int(s) for s in input().split())
challenges = deque(int(c) for c in input().split())

while True:
    if challenges:
        if not tools or not substances:
            print('Harry is lost in the temple. Oblivion awaits him.')
            break
    else:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

    result = tools[0] * substances[-1]

    if result in challenges:
        tools.popleft()
        substances.pop()
        challenges.remove(result)
    else:
        tools[0] += 1
        tools.rotate(-1)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()

if tools:
    formatted_tools = ', '.join(str(tool) for tool in tools)
    print(f"Tools: {formatted_tools}")
if substances:
    formatted_substances = ', '.join(str(substance) for substance in substances)
    print(f"Substances: {formatted_substances}")
if challenges:
    formatted_chalenge = ', '.join(str(challenge) for challenge in challenges)
    print(f"Challenges: {formatted_chalenge}")
