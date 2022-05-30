r=int(input('Enter rows :'))
for i in range (1,r+1,1):
    for j in range(1,i+1,1):
        print('* ',end="")
    print()
for i in range(r,0,-1):
    for j in range(1,i+1,1):
        print('* ',end="")
    print()
