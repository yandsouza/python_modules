from collections.abc import Callable
from functools import reduce, partial, singledispatch, lru_cache
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        op_function = operator.add
    elif operation == "multiply":
        op_function = operator.mul
    elif operation == "max":
        op_function = max
    elif operation == "min":
        op_function = min
    else:
        raise ValueError("Invalid operation.")
    return reduce(op_function, spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} spell hits {target} for {power} HP"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    wind_enchant = partial(base_enchantment, power=50, element="Wind")
    fire_enchant = partial(base_enchantment, power=50, element="Fire")
    water_enchant = partial(base_enchantment, power=50, element="Water")
    return {
        "wind": wind_enchant,
        "fire": fire_enchant,
        "water": water_enchant
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def spell_system(spell: Any) -> str:
        return "Unknown spell type"

    @spell_system.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @spell_system.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @spell_system.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return spell_system


if __name__ == "__main__":
    print("===========Ancient Library=========")
    print()

    spell_powers = [10, 30, 40, 20]
    try:
        print(f"Sum: {spell_reducer(spell_powers, "add")}")
        print(f"Product: {spell_reducer(spell_powers, "multiply")}")
        print(f"Max: {spell_reducer(spell_powers, "max")}")
        print(f"{spell_reducer(spell_powers, "invalid")}")
    except ValueError as error:
        print(error)
    print()

    enchants = partial_enchanter(base_enchantment)
    print(enchants["wind"](target="Dragon"))
    print(enchants["fire"](target="Orc"))
    print(enchants["water"](target="Fairy"))
    print()

    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Cache info:", memoized_fibonacci.cache_info())
    print("Fib(15):", memoized_fibonacci(15))
    print("Fib(15):", memoized_fibonacci(15))
    print("Cache info:", memoized_fibonacci.cache_info())
    print()

    spell_system = spell_dispatcher()
    print(spell_system(42))
    print(spell_system("fireball"))
    print(spell_system(["fireball", "heal", "magic shield"]))
    print(spell_system({"unknown": "spell"}))
