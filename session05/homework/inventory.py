inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll","bread loaf"]
}
print (inventory)
print ("add pocket")
inventory["pocket"] = ["seashell", "strange berry", "lint"]
print (inventory)
print ("remove dagger from backpack")
inventory["backpack"].remove("dagger")
print (inventory)
print ("add + 50 to pocket")
inventory["gold"] += 50
print (inventory)