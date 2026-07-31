import math


def validade_list(cord: str) -> float | None:
    try:
        return float(cord)
    except ValueError:
        print(f"Error on parameter '{cord}': "
              f"could not convert string to float: '{cord}'")
        return None


def get_player_pos() -> tuple[float, float, float]:
    while True:
        cords_input = input("Enter new coordinates as "
                            "floats in format 'x,y,z': ")
        cords = cords_input.split(',')

        if len(cords) != 3:
            print("Invalid syntax")
            continue

        values = []
        for cord in cords:
            value = validade_list(cord)
            if value is None:
                break
            values.append(value)

        if len(values) != 3:
            continue

        return values[0], values[1], values[2]


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    player_pos = get_player_pos()
    x1, y1, z1 = player_pos[0], player_pos[1], player_pos[2]
    print(f"Got a first tuple: {player_pos}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)
    print(f"Distance to center: {distance}")
    print()

    print("Get a second set of coordinates")
    player_pos = get_player_pos()
    x2, y2, z2 = player_pos[0], player_pos[1], player_pos[2]

    distance_3d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_3d}")
