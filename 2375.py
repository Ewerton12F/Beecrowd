#2375

n=int(input())
A,L,P=map(int,input().split())

if n <= A and n <= L and n <= P:
  print("S")
else:
  print("N")