from ex0.creature_factory import AquaFactory, CreatureFactory, FlameFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2.strategy import BattleStrategy, DefensiveStrategy, NormalStrategy, \
                         StrategyError, AggressiveStrategy


def battle(creatures: list[tuple[CreatureFactory, BattleStrategy]],) -> None:
    fighters = [(factory.create_base(), strategy)
                for factory, strategy in creatures]
    battles = [f"({creature.name}+"
               f"{strategy.__class__.__name__.removesuffix('Strategy')})"
               for creature, strategy in fighters]
    print(f" [ {", ".join(battles)} ]")
    print("*** Tournament ***")
    print(f"{len(creatures)} opponets involved")
    print()

    for i in range(len(creatures)):
        for e in range(i + 1, len(creatures)):
            factory_1, strategy_1 = creatures[i]
            factory_2, strategy_2 = creatures[e]

            print("* Battle *")
            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()
            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            print(" now fight!")
            try:
                print(strategy_1.act(creature_1))
                print(strategy_2.act(creature_2))
            except StrategyError as e:
                print("Battle error, aborting tournament:", e)
            print()


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    creatures_list = [(FlameFactory(), NormalStrategy()),
                      (HealingCreatureFactory(), DefensiveStrategy())]
    battle(creatures_list)
    print()

    print("Tournament 1 (error)")
    creatures_list2 = [(FlameFactory(), AggressiveStrategy()),
                       (HealingCreatureFactory(), DefensiveStrategy())]
    battle(creatures_list2)
    print()

    print("Tournament 2 (multiple)")
    creatures_list3 = [(AquaFactory(), NormalStrategy()),
                       (HealingCreatureFactory(), DefensiveStrategy()),
                       (TransformCreatureFactory(), AggressiveStrategy())]
    battle(creatures_list3)
