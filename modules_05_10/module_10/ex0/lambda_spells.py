def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda art: art['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": int(max(
            mages, key=lambda mage: mage["power"])["power"]),
        "min_power": int(min(
            mages, key=lambda mage: mage["power"])["power"]),
        "avg_power": sum(map(
            lambda mage: int(mage["power"]), mages)) / len(mages)}


if __name__ == "__main__":
    artifacts = [
        {'name': 'Light Prism', 'power': 108, 'type': 'accessory'},
        {'name': 'Lightning Rod', 'power': 114, 'type': 'relic'},
        {'name': 'Lightning Rod', 'power': 68, 'type': 'relic'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'accessory'}]
    mages = [
        {'name': 'Storm', 'power': 88, 'element': 'water'},
        {'name': 'Phoenix', 'power': 94, 'element': 'fire'},
        {'name': 'River', 'power': 99, 'element': 'earth'},
        {'name': 'Rowan', 'power': 95, 'element': 'ice'},
        {'name': 'Morgan', 'power': 59, 'element': 'light'}]
    spells = ['tornado', 'blizzard', 'meteor', 'freeze']

    def print_result(result: list[dict] | list[str] | dict) -> None:
        for data in result:
            print("", data)
        print()

    print("==========Lambda Sanctum==========")
    print()

    print("Sort magical artifacts by ’power’ level (descending):")
    print_result(artifact_sorter(artifacts))

    print("Filter mages by power >= 91:")
    print_result(power_filter(mages, 91))

    print("Transform spell names to add '* ' prefix and ' *' suffix:")
    print_result(spell_transformer(spells))

    print("Calculate statistics:")
    for key, value in mage_stats(mages).items():
        print(f" {key}: {value}")
