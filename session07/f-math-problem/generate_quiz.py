
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
    error = [-1,0,0,0,0,0,0,1]
    ran_error = choice(error)
    ans = res + ran_error
    return [x, y, op, ans]