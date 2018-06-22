from turtle import*
color("red")

for i in range(4):
    for _ in range(2):
        right (300)
        forward(100)
    left(60)
    for _ in range(2):
        left (60)
        forward(100)
    right (30)
    
mainloop()