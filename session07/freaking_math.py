from random import randint, choice
# from evaluate import calculate
import evaluate
x = randint(0,10)
y = randint(1,10)
op =choice(["+","-","*","/"])
res = evaluate.calculate(x,y,op)
error = [-1,0,0,0,0,0,0,1]
ran_error = choice(error)
ans = res + ran_error
print ("{0} {1} {2} = {3}".format(x,op,y,ans))
user = input ("(Y/N): ").lower()

if ran_error == 0:
    if user == "y":
        print ("Yay")
    elif user == "n":
        print ("wrong answer")
else:
    if user == "n":
        print ("Yay")
    elif user == "y":
        print ("wrong answer")

