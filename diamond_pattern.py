p=1
for i in range(5,0,-1):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0, p):
        print("*", end="")
    p=p+2
    print()

p=9
for i in range(1,7):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0, p):
        print("*", end="")
    p=p-2
    print()
