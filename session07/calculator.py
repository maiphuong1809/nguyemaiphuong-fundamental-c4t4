x = float(input("x = "))
operation = input("operation(+,-,*,/):")
y = float (input("y = "))
# if operation == "+" :
#     print ("{0} {1} {2} = {3}").format (x,operation,y,x+y)
# elif operation == "-":
#     print ("{0} {1} {2} = {3}").format (x,operation,y,x-y)
# elif operation == "*":
#     print ("{0} {1} {2} = {3}").format (x,operation,y,x*y)
# elif operation == "/":
#     print ("{0} {1} {2} = {3}").format (x,operation,y,x/y)
# else:
#     print ("wrong operation")

if operation == "+":
    res = x + y
elif operation == "-":
    res = x - y
elif operation == "*":
    res = x * y
elif operation == "/":
    res = x / y

print ("*"*20)
print ("{0} {1} {2} = {3}".format (x,operation,y,res))
print ("*"*20)