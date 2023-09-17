petrol_pump_number = int(input())
deque_list = []

for pump in range(petrol_pump_number):
    input_value = input().split()
    petrol = int(input_value[0])
    distance = int(input_value[1])
