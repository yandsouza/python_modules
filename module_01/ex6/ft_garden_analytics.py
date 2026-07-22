class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._count_grow = 0
            self._count_age = 0
            self._count_show = 0

        def inc_grow_stat(self) -> None:
            self._count_grow += 1

        def inc_age_stat(self) -> None:
            self._count_age += 1

        def inc_show_stat(self) -> None:
            self._count_show += 1

        def show(self) -> None:
            print(f"Stats: {self._count_grow} grow,"
                  f" {self._count_age} age,"
                  f" {self._count_show} show")

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth: float,
    ):
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth
        self._statistics = self.Statistics()

    def show(self) -> None:
        self._statistics.inc_show_stat()
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._statistics.inc_grow_stat()
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
        self._statistics.inc_age_stat()
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

    @staticmethod
    def check_year_old(age: int) -> None:
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    def show_statistics(self) -> None:
        print(f"[statistics for {self._name}]")
        self._statistics.show()


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

    def bloom_grow(self) -> None:
        self.blooming = True
        self.grow()
        print(f"[asking the {self._name} to grow and bloom]")

    def bloom_grow_age(self, days: int) -> None:
        self.blooming = True
        self._statistics.inc_age_stat()
        self._statistics.inc_grow_stat()
        for day in range(days):
            self._age += 1
            self._height += self._growth
        print(f"[make {self._name} grow, age and bloom]")


class Seed(Flower):
    seeds: int = 0

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth: float,
            color: str,
            seeds_to_bloom: int
    ):
        super().__init__(name, height, age, growth, color)
        self.seeds_to_bloom = seeds_to_bloom

    def bloom_grow_age(self, days: int) -> None:
        super().bloom_grow_age(days)
        if self._age > 60 and days > 10:
            self.seeds += self.seeds_to_bloom

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._count_shade = 0

        def inc_shade_stat(self) -> None:
            self._count_shade += 1

        def show(self) -> None:
            super().show()
            print(f" {self._count_shade} shade")

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
        self._statistics: Tree.TreeStatistics = Tree.TreeStatistics()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._statistics.inc_shade_stat()
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height:.1f}cm "
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


def show_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._statistics.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year_old(30)
    Plant.check_year_old(500)
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    rose.show_statistics()
    rose.bloom_grow()
    rose.show()
    rose.show_statistics()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.2, 5.0)
    oak.show()
    oak.show_statistics()
    oak.produce_shade()
    oak.show_statistics()
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 1.5, "yellow", 42)
    sunflower.show()
    sunflower.bloom_grow_age(20)
    sunflower.show()
    sunflower.show_statistics()
    print()
    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    show_statistics(unknown)
