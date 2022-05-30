r=int(input('Enter rows :'))
for i in range (1,r+1,1):
    for j in range(1,r-i+2,1):
        print('* ',end="")
    print(
