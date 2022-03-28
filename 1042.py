#1042

n1,n2,n3=map(int, input().split())
p = s = t = 0

if n1 < n2 and n1 < n3:
  p = n1

if n2 < n1 and n2 < n3:
  p = n2

if n3 < n1 and n3 < n2:
  p = n3


if n2 > n1 > n3 or n3 > n1 > n2:
  s = n1
elif n1 > n2 > n3 or n3 > n2 > n1:
  s = n2
elif n1 > n3 > n2 or n2 > n3 > n1:
  s = n3

if n1 > n2 and n1 > n3:
  t = n1

if n2 > n1 and n2 > n3:
  t = n2

if n3 > n1 and n3 > n2:
  t = n3


print(f"{p}\n{s}\n{t}\n")
print(f"{n1}\n{n2}\n{n3}")