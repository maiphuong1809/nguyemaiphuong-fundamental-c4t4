from turtle import*
speed (-1)
color("blue")

for i in range (50):
    for _ in range (4):
        forward (20+i*4)
        left (90)
    right (350)

mainloop()