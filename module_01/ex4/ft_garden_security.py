class Plant:
    def __init__(self, name, height, age, growth):
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self):
        self.height += self.growth

    def set_height(self, height):
        if height < 0: 
            print(f"{self._name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self._height)}cm")

    def get_height(self):
        return self._height

    def set_age(self, age):
        if age < 0: 
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def get_age(self):
        return self._age

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
            week_growth += self._growth
        print(f"Growth this week: {week_growth}cm")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10, 0.8)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-25.0)
    rose.set_age(-30)
    print()
    print("Current state: ", end="")
    rose.show()
