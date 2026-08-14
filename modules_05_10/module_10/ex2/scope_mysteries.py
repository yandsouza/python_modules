from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulator(adder: int) -> int:
        nonlocal power
        power += adder
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("==========Memory Depths==========")
    print()

    print("Create a counting closure:")
    counter = mage_counter()
    for _ in range(5):
        print(counter())
    print()

    print("Create power accumulator:")
    accumulator = spell_accumulator(0)
    for _ in range(10):
        print(accumulator(5))
    print()

    print("Create enchantment functions:")
    frozen = enchantment_factory("Frozen")
    windy = enchantment_factory("Windy")
    earthen = enchantment_factory("Earthen")
    print(frozen("Shield"))
    print(windy("Sword"))
    print(earthen("Armor"))
    print()

    print("Create a memory management system:")
    memory = memory_vault()
    memory["store"]("secret", "42")
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {memory['recall']('secret')}")
    print(f"Recall 'unknown': {memory['recall']('unknown')}")
