from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__[T](self, name: str, creature_type: T):
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self):
        pass

    def describe[T](self, name: str, creature_type: T):
        return f"{self.name} is a {self.creature_type} type Creature"
