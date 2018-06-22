from turtle import*

speed(-1)
for i in range (100):
    #forward(10)
    for _ in range (4):
        forward (10+i*4)
        right(90)
    left(10)


mainloop()