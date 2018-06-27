num = int(input("Enter a number: "))
Sum = 0
for i in range (1, num+1):
    Sum = Sum + 1/i
   
print("the sum of :S= 1/1 + 1/2 +...+ 1/{0}{1}{2}".format(num," = ",Sum))