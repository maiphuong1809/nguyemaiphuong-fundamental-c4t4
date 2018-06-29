favourite = ["films","facebook","sports"]
position = int(input("position you want to update:"))
thing = input("Your replacing favourite:")
favourite [position-1]= thing
print ("* " * 20)
for index, item in enumerate(favourite):
    print (index+1,item,sep=".")
print ("* " * 20)