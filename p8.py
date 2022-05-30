#Pattern 8
a=1
j=int(input("Enter no. of rows: "))
sp=j-1
for i in range(0,j):
    print("  "*sp+" *"*a,end='')
    sp-=1
    a+=2
    print("\n")
