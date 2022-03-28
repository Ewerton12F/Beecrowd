#1019

n = int(input())

hour = n // 3600
min = (n // 60) % 60
sec = n % 60

print(f'{hour}:{min}:{sec}')