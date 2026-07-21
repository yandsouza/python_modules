class Plant:
    def __init__(self, name: str, height: float, age: int, growth: float):
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def age_day(self) -> None:
        self.age += 1

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
            week_growth += self.growth
        print(f"Growth this week: {week_growth:.1f}cm")


def plant_factory() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 0.2),
        Plant("Cactus", 5.0, 90, 0.6),
        Plant("Sunflower", 5.0, 90, 0.5),
        Plant("fern", 15.0, 120, 0.3)]

    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_factory()
