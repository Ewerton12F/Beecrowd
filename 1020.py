#1020

age_days = int(input())

years = age_days // 365
months = (age_days % 365) // 30
days = (age_days % 365) % 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')