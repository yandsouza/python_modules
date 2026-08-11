from ex0 import CreatureFactory, FlameFactory, AquaFactory


def verify_factory(factory: CreatureFactory) -> None:
    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()
    print(creature_1.describe())
    print(" vs.")
    print(creature_2.describe())
    print(" fight!")
    print(creature_1.attack())
    print(creature_2.attack())


if __name__ == "__main__":
    flame_creature = FlameFactory()
    aqua_creature = AquaFactory()

    print("Testing factory")
    verify_factory(flame_creature)
    print()

    print("Testing factory")
    verify_factory(aqua_creature)
    print()

    print("Testing battle")
    battle(flame_creature, aqua_creature)
