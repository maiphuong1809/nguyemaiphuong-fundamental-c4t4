from turtle import*


for i in range(3,8):
    for k in range (i):
        if i == 3:
            color ("red")
        elif i == 4:
            color ("blue")
        elif i == 5:
            color ("brown")
        elif i == 6:
            color ("yellow")
        else:
            color ("gray")
        forward(100)
        left(360/i)

mainloop()