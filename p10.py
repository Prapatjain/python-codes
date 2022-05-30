# Pattern 10
rows=int(input("Enter number of rows: "))
clm=int(input("Enter number of columns: "))
ch=input("Enter any character: ")
for i in range(rows):
    for j in range(clm):
        if(i==0 or i==rows-1 or j==0 or j==clm-1):
            print('%c'%ch,end='')
        else:
            print('',end=' ')
    print()
