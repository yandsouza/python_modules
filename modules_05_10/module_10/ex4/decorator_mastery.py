from collections.abc import Callable
from functools import wraps
import time
import random


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", args[-1] if args else 0)
            if power < min_power:
                return "Insufficient power"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spellcasting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        name_no_space = name.replace(" ", "")
        return len(name_no_space) >= 3 and name_no_space.isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("=========Master’s Tower=========")
    print()

    print("Time execution decorator:")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Result: Fireball cast!"
    print(fireball())
    print()

    print("Parameterized validation decorator:")

    @power_validator(25)
    def spell_caster(spell: str, power: int) -> str:
        return f"{spell} casted with power {power}"
    print(spell_caster("Water Blast", 50))
    print(spell_caster("Water Blast", 5))
    print()

    print("Retry decorator:")

    @retry_spell(3)
    def retrying_spell():
        if random.random() < 0.8:
            raise ValueError("Spell not casted!")
        return "Waaaaaaagh spelled !"

    print(retrying_spell())
    print()

    print("Demonstrate staticmethod:")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("John"))
    print(MageGuild.validate_mage_name("Jo35"))
    print(guild.cast_spell("Fire", 15))
    print(guild.cast_spell("Water", 5))
