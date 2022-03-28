#1929

L1,L2,L3,L4=map(float, input().split())

if L1 + L2 > L3 and L2 + L3 > L1 and L1 + L3 > L2:
    print('S')
elif L2 + L3 > L4 and L3 + L4 > L2 and L2 + L4 > L3:
    print('S')
elif L1 + L3 > L4 and L3 + L4 > L1 and L1 + L4 > L3:
    print('S')
elif L1 + L2 > L4 and L2 + L4 > L1 and L1 + L4 > L2:
    print('S')
else:
    print('N')