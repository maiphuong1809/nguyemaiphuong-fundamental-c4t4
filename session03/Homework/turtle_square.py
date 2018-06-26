from turtle import*
import random

speed (-1)
shape ("turtle")

colors = ["black", "grey"]
for i in range (1,101):
    c = random.choice(colors)
    forward (i*4)
    left(90)
    color(c)
          
mainloop()
