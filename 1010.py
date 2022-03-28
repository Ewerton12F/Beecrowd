#1010

p1, p1u, p1p = input().split()
p2, p2u, p2p = input().split()

cp1 = int(p1)
cp1u = int(p1u)
cp1p = float(p1p)

cp2 = int(p2)
cp2u = int(p2u)
cp2p = float(p2p)

amount1 = cp1u * cp1p
amount2 = cp2u * cp2p

total = amount1 + amount2

print(f'VALOR A PAGAR: R$ {total:.2f}')