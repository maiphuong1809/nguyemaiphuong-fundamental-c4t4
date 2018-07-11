from turtle import*

for i in range(4,10):
    for k in range (i):
        if k%2 == 1:
            color("blue")
        else:
            color("red")
        forward(100)
        left(360/i)
    

mainloop()