#1046

start,end=map(int,input().split())
dur = 0

if start > 12 and start > end:
  dur = 24 - start + end

if start < end:
  dur = end - start

if start == end:
  dur = 24

print(f"O JOGO DUROU {dur} HORA(S)")