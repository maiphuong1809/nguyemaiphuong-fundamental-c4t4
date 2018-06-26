from random import randint
mood = randint(0,100)
print ("Hi, my name is mr moody")
if mood <30:
    print("I feel sad :<")
elif mood <60:
    print("I feel ok")
else:
    print("Oh yeah, I'm happy :>")