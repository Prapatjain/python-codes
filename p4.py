#Pattern 4
n=int(input())
sp=0
for i in range(n,0,-1):
    print(" "*sp+"*"*i,end="")
    sp+=1
    print()
