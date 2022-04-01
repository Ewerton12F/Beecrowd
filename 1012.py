# https://www.beecrowd.com.br/judge/en/problems/view/1012

a, b, c = map(float, input().split())
pi = 3.14159

a1 = (a*c) / 2 # the area of the rectangled triangle that has base A and height C.
b1 = pi * (c**2) # the area of the radius's circle C. 
c1 = 0.5 * (a+b) * c # the area of the trapezium which has A and B by base, and C by height.
d1 = b ** 2 # the area of the square that has side B.
e1 = a * b # the area of the rectangle that has sides A and B.


print(f'TRIANGULO: {a1:.3f}')
print(f'CIRCULO: {b1:.3f}')
print(f'TRAPEZIO: {c1:.3f}')
print(f'QUADRADO: {d1:.3f}')
print(f'RETANGULO: {e1:.3f}')