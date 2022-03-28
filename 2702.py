#2702

Ca,Ba,Pa=map(int,input().split())
Cr,Br,Pr=map(int,input().split())
req=0

if Ca < Cr:
  req+=Ca-Cr
if Ba < Br:
  req+=Ba-Br
if Pa < Pr:
  req+=Pa-Pr

print(-req)