num = int(input("Enter total number of 1's and 0's:"))
if num/2 ==0:
    for i in range(num/2):
        print("1 0", end=" ")
else :
    for i in range(int((num-1)/2)):
        print("1 0", end=" ")
    print(1)
