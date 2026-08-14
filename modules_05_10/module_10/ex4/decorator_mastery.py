from collections.abc import Callable
from functools import wraps
from typing import Any
import time

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
                return "Insufficient power for this spell"
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
        clean_name = name.replace(" ", "")
        return len(clean_name) >= 3 and clean_name.isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def spell_caster(spell: str, damge: int) -> str:
        time.sleep(0.2)
        return f"{spell} casted and {damge} done"

    print(spell_caster("Fire", 200))

    print("\n## Testing power_validator...\n")

    @power_validator(100)
    def powerful_spell(spell: str, power: int) -> str:
        return f"{spell} casted with power {power}"
    print(powerful_spell("Lightning", 150))
    print(powerful_spell("Lightning", 50))

    print("\n## Testing retry_spell...\n")

    @retry_spell(5)
    def retrying_spell():
        raise ValueError("boom")
    print(retrying_spell())

    print("\n## Testing power_validator...\n")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("ahmad"))
    print(MageGuild.validate_mage_name("9x"))
    print(guild.cast_spell("Fire", 15))
    print(guild.cast_spell("Water", 5))
