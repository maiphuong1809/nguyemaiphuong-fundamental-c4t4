
print ("Guess your number")
enter = input ("Now think of a number from 1 to 100, then press enter")
print (" ")
print ("All your have to do is ask my guess ")
print ("c: if my guess is correct")
print ("s: if my guess is (s)maller than your number")
print ("l: if my guess is (l)arger than your number")
low = 0 
high = 100 
trial = 0
comp = 50
loop = True
while loop:
    ans = input ("Is {0} your number ?".format(comp))
    if ans == "l":
        high = comp
        comp = (high + low)//2
    elif ans == "s":
        low = comp
        comp = (low + high)//2
    else :
        print ("I knew it ")
        break