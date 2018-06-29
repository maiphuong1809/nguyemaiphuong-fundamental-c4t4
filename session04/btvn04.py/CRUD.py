print("welcome to our shop, what do you want")
ans = input ("(C, R, U, D) ? ").upper()
our_item = ["T-shirt","Sweater"]
if ans == "R":
    print ("Our item:",*our_item, sep = ", ")
elif ans == "C":
    new_item = input ("Enter new item: ")
    our_item.append(new_item)
    print ("Our item:",*our_item, sep = ", ")
elif ans == "U":
    update_pos = int(input("Update position: "))
    new = input ("New item :")
    del our_item[update_pos-1]
    our_item.append(new)
    print ("Our item:",*our_item, sep = ", ")
elif ans == "D":
    delete_pos = int(input ("Delete position: "))
    del our_item[delete_pos-1]   
    print ("Our item:",*our_item, sep = ", ")
else:
    print ("wrong command!")


