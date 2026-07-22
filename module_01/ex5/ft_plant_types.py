class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth: float
    ):
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self._growth

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height:.1f}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def get_age(self) -> int:
        return self._age

    def age_day(self) -> None:
        self._age += 1

    def growth_day(self) -> None:
        self.grow()
        self.age_day()

    def growth_week(self, days: int) -> None:
        week_growth: float = 0
        self.show()
        for day in range(days):
            self.growth_day()
            print(f"=== Day {day + 1} ===")
            self.show()
            week_growth += self._growth
        print(f"Growth this week: {week_growth:.1f}cm")


class Flower(Plant):
    blooming: bool = False

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth: float,
            color: str
    ):
        super().__init__(name, height, age, growth)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        self.blooming = True
        print(f"[asking the {self._name} to bloom]")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth: float,
            trunk_diameter: float
    ):
        super().__init__(name, height, age, growth)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]\n"
              f"Tree {self._name} now produces "
              f"a shade of {self._height:.1f}cm "
              f"long and {self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth: float,
            harvest_season: str,
            nutritional_value: int
    ):
        super().__init__(name, height, age, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def growth_week(self, days: int) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        for day in range(days):
            self.growth_day()
            self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.8, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.2, 5.0)
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0)
    tomato.show()
    tomato.growth_week(20)
    tomato.show()
