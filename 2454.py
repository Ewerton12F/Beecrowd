#2454

P,R=map(int,input().split())

if P == 0:
  print("C")

if P == 1:
  if R == 0:
    print("B")
  if R == 1:
    print("A")