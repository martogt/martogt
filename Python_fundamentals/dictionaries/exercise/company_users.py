company_info = {}

while True:
    line_input = input()
    if line_input == "End":
        break

    company, employee_id = line_input.split(" -> ")

    if company not in company_info:
        company_info[company] = []
    company_info[company].append(employee_id)

for company, employee_id in company_info.items():
    print(f"{company}")
    for employee_id in company:
        print(company_info[employee_id])
