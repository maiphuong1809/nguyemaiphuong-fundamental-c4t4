from turtle import*

speed(-1)
shape ("turtle")
color("green")
for i in range (10):
    pendown()
    circle(10+i*8)
    penup()

mainloop()