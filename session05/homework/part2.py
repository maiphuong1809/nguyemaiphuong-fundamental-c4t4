prices = {
    "banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock = {
    "banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
total = 0.0
for fruit in stock:
    print (fruit)
    print ("Price:{0}".format(prices[fruit]))
    print ("Stock:{0}".format(stock[fruit]))
    print ()
    total += stock[fruit]*prices[fruit] 
print ("Total:{0}".format(total))
