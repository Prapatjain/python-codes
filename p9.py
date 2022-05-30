#Pattern 9
n=int(input("Enter number of rows: "))
sp=n-1
for i in range(1,n+1):
    print(" "*sp+"*"*i+" "*(sp+1)+"*"*i)
    sp-=1
    print()
