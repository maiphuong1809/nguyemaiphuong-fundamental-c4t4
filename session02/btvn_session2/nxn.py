n = int(input("Enter a number: "))
for x in range(1,n+1):
    for y in range(1,n+1):
        z = x*y
        print(z,end="\t")
    print()
