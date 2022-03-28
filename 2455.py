#2455

P1,C1,P2,C2=map(int,input().split())

if P1 * C1 == P2 * C2:
  print(0)

if P1 * C1 < P2 * C2:
  print(1)

if P1 * C1 > P2 * C2:
  print(-1)