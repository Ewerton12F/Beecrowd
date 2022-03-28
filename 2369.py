#2369

n = int(input())

if n <= 10:
  n=7
  print(n)

elif 11 <= n <= 30:
  n-=10
  n+=7
  print(n)

elif 31 <= n <= 100:
  n-=30
  n*=2
  n+=27
  print(n)

elif 101 <= n:
  n-=100
  n*=5
  n+=167
  print(n)