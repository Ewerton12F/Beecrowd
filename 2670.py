#2670

a1=int(input())
a2=int(input())
a3=int(input())

t1 = a1*0 + a2*2 + a3*4
t2 = a1*2 + a2*0 + a3*2
t3 = a1*4 + a2*2 + a3*0

if(t1<=t2):
  menor=t1
else:
  menor=t2
if(menor>=t3):
  menor=t3

print(menor)