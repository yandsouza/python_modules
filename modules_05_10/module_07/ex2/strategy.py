from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class StrategyError(Exception):
    def __init__(self, message: str = "Unknown strategy error"):
        self.message = message
        super().__init__(self.message)


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy.")
        return f"{creature.transform()}\n" \
               f"{creature.attack()}\n" \
               f"{creature.revert()}"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not isinstance(creature, HealCapability):
            raise StrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy.")
        return f"{creature.attack()}\n" \
               f"{creature.heal()}"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
