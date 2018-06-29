
num = [-1,-10,-100,20, 0]
new_num = []
while True:
    if len(num) !=0:
        new_num.append (min(num))
        num.remove (min(num))
    else:
        print (*new_num, sep = ", ")
        break


    
