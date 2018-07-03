map = {
    "size_x":5,
    "size_y":5
}

player ={"x":2,"y":4}
boxes = [
    {"x":1,"y":1},
    {"x":2,"y":2},
    {"x":3,"y":3},
]
destinations = [
    {"x":2,"y":1},
    {"x":3,"y":2},
    {"x":4,"y":3},
]

for y in range (map["size_y"]):
    for x in range(map["size_x"]):
        box_is_here = False
        for box in boxes:
            if box['x']== x and box['y']== y:
                box_is_here = True
        
        player_is_here = False
        if x== player["x"] and y ==player["y"]:
            player_is_here = True
        
        dest_is_here = False
        for destination in destinations :
            if destination['x']== x and destination['y']== y:
                dest_is_here = True

        if box_is_here == True:
            print("B ", end = "")
        elif player_is_here == True:
            print("P ", end = "")
        elif dest_is_here == True:
            print("D ", end = "")
        else:
            print("- ",end="")
    print()

