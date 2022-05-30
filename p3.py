#Pattern 3
n=int(input())
sp=n-1
for i in range(1,n+1):
    print(" "*sp+"*"*i,end="")
    sp-=1
    print()
