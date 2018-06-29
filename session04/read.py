favourite = ["films","facebook","sports"]
print (*favourite, sep=", ")
print ("* " * 20)
for index, item in enumerate(favourite):
    print (index+1,item,sep=".")
print ("* " *20)