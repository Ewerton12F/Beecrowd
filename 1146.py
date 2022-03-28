#1146

while True:
  n = int(input())
  if n == 0:
    break
  for i in range(1,n+1):
    print(i, end='')
    print(' ' if i < n else '\n', end='')