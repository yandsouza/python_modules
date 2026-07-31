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


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    rose.growth_week(16)
