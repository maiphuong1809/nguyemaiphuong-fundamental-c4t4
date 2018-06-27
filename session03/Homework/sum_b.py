num = int(input("Enter a number: "))
Sum = 0
for i in range (1, num+1):
    m=1
    for p in range(1,i+1):
        m=m*p    
    Sum=Sum+1/m 
   
print("S = 1/1! + 1/2! + ... + 1/{0}{1}{2}".format(num,"! = ",Sum))