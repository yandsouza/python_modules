from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def mega_spell(target: str, power: int) -> Callable:
        return (base_spell(target, (power * multiplier)))
    return mega_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> Callable | str:
        if condition(target, power) is True:
            return (spell(target, power))
        else:
            return ("Spell fizzled")
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball damages {target} for {power} HP"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def magic_shield(target: str, power: int) -> str:
        return f"Magic Shield protect {target} for {power} HP"

    print("==========Higher Realm==========")
    print()

    print("Combine two spells:")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 25))
    print()

    print("Amplify spell power:")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 25))
    print()

    print("Cast spell conditionally (power >= 15):")

    def condition(target, power) -> bool:
        if power >= 15:
            return True
        return False

    conditional_spell = conditional_caster(condition, fireball)
    print("'Power == 25':")
    print(conditional_spell('Dragon', 25))
    print("'Power == 11':")
    print(conditional_spell('Dragon', 11))
    print()

    print("Create spell sequence:")
    sequence = spell_sequence([heal, fireball, magic_shield])
    sequence_list = sequence("Dragon", 25)
    for spell in sequence_list:
        print(spell)
