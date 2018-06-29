print ("Hi there, here are you favourite things so far")
favourite = ["films","facebook","sports"]
print (*favourite, sep=", ")
thing = input("name one thing you want to add: ")
favourite.append(thing)
print (*favourite, sep=", ")