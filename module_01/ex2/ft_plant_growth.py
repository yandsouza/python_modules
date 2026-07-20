class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += self.growth

    def age_day(self):
        self.age += 1

    def growth_day(self):
        self.grow()
        self.age_day()

    def growth_week(self, days):
        week_growth = 0
        self.show()
        for day in range(days):
            self.growth_day()
            print(f"=== Day {day} ===")
            self.show()
            week_growth += self.growth
        print(f"Growth this week: {week_growth}cm")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30, 0.8)
    rose.growth_week(7)
