import sys


def create_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    args = sys.argv[1:]
    for arg in args:
        try:
            item, num = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if item in inventory.keys():
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            inventory.update({item: int(num)})
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
    return inventory


def items_quantity(inventory: dict[str, int]) -> None:
    most = None
    least = None
    name_most = None
    name_least = None

    for item in inventory:
        quantity = inventory[item]
        if most is None or quantity > most:
            most = quantity
            name_most = item
        if least is None or quantity < least:
            least = quantity
            name_least = item

    print(f"Item most abundant: {name_most} with quantity {most}")
    print(f"Item least abundant: {name_least} with quantity {least}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory = create_inventory()
    print(f"Got inventory: {inventory}")

    item_list = inventory.keys()
    print(f"Item list: {list(item_list)}")

    item_total = sum(list(inventory.values()))
    print(f"Total quantity of the {len(list(inventory.values()))} "
          f"items: {item_total}")

    for item in inventory:
        percent = round(((inventory[item] * 100) / item_total), 1)
        print(f"Item {item} represents {percent}%")

    items_quantity(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
