r=int(input('Enter rows :'))
for i in range (1,r+1):
    for j in range(1,r-i+1,1):
        print(' ',end="")
    for j in range(1,i+1,1):
        print('*',' ',end="")
    print()
