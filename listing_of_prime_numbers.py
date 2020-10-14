final=int(input("Enter the range upto which the prime nos are to be calculate"))
count=False
for i in range(1,final+1):
    count = False
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            count = True
    if not count:
        if i!=1:
            print(i)
