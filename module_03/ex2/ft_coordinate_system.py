def get_player_pos():
    cords = input("Enter new coordinates as floats in format 'x,y,z': ")
    cords = tuple(int(x) for x in cords.split(','))
    print(cords)
    return cords

get_player_pos()
