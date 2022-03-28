#1008

employee_number = int(input())
worked_hours = int(input())
amount_per_hour = float(input())

employee_salary = worked_hours * amount_per_hour

print(f'NUMBER = {employee_number}')
print(f'SALARY = U$ {employee_salary:.2f}')