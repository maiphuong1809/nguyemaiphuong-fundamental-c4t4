from random import *

# def generate_quiz():
#     # Hint: Return [x, y, op, result]
#     return [3, 5, '+', 8]

def generate_quiz():
    from random import randint, choice
    x = randint(0,10)
    y = randint(1,10)
    op =choice(["+","-","*","/"])
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    elif op == "/":
        res = x / y
    error = [-1,0,0,1]
    ran_error = choice(error)
    result = res + ran_error
    return [x, y, op, result]
    
# import generate_quiz
def check_answer(x, y, op,result, user_choice):
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    elif op == "/":
        res = x / y
   
    if result == res:
        choice = True
    else:
        choice = False
    return bool(choice==user_choice)
# IF user choice = true return true