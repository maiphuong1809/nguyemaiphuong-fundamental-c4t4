from random import choice
playing = True
words = {"champion","depression","utopia","coding","conduct"}
word = list(words)
ran_word = choice(word)
char = list(ran_word)
while playing:
    ran_char = choice (char)
    print (ran_char, end = " ")
    char.remove (ran_char)
    if len(char) == 0:
        break
print ()

while True:
    ans = input ("Enter your answer:")
    if ans == ran_word:
        print ("Hura")
        break
    else:
        print ("=((((")
