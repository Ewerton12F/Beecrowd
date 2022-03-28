#1893

d1,d2 = map(int,input().split())

if 0 <= d1 and d2 <= 2:
  print("nova")

elif d1 < d2 and d2 <= 96:
  print("crescente")

elif d1 >= d2 and d2 <= 96:
  print("minguante")

else:
  print("cheia")