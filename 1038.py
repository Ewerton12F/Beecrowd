#1038

code, price = input().split()

X = int(code)
Y = int(price)
t = 0

if X == 1:
  t = Y * 4.00  
elif X == 2:
  t = Y * 4.50  
elif X == 3:
  t = Y * 5.00  
elif X == 4:
  t = Y * 2.00  
elif X == 5:
  t = Y * 1.50  

print(f'Total: R$ {t:.2f}')