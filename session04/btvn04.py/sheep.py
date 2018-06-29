
sheep_size = [20,15,10,4, 78,100, 60,50]
print ("Hi, my name is AI and these are my sheep size:",sheep_size)
max1 = max(sheep_size)

print ("Now my biggest sheep has size {0} let's shear it".format(max1))
sheep_size[sheep_size.index(max1)] =8
print ("After shearing , here is my flock", sheep_size)

for j in range (2):
    print ("MONTH",j+1)
    print ("One month passed, here is my flock")
    for i in range (len(sheep_size)):
        sheep_size[i] += 50
    print(sheep_size)
    max2 = max(sheep_size)
    print ("Now my biggest sheep has size {0} let's shear it".format(max2))
    sheep_size[sheep_size.index(max2)] =8
    print ("After shearing , here is my flock", sheep_size)
total = 0
for i in range (7):
    total = sheep_size[i] + total
print ("my flock has size in total :",total)
print ("Iwill have:",total*2,"$")
