from random import randint
numb = randint (1,100)
count = 0
loop = True
while loop:
    guess = int(input ("Guess my number (1-100): "))
    if numb < guess <(numb + 15):
        print ("A little too large ")
    elif guess > (numb + 16):
        print ("too large")
    elif (numb - 15) < guess < (numb-1):
        print ("A little too small ")
    elif guess < (numb - 16):
        print ("too small")
    else :
        print ("bingo")
        break
    count +=1
    if count == 7:
        print ("Game over")
        loop = False 
