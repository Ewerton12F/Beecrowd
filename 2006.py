#2006

T = int(input())
A,B,C,D,E=map(int, input().split())
correct=0

if A == T:
  correct+=1
if B == T:
  correct+=1
if C == T:
  correct+=1
if D == T:
  correct+=1
if E == T:
  correct+=1

print(correct)