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
        self.age += 1

    def plant_factory(self, st_name, st_height, st_age):
        inventory = []
        new_plant = Plant(st_name, st_height, st_age)
        inventory.append(new_plant)
        return inventory

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30, 0.8)
    oak = Plant("Oak", 200, 365, 0.8)
    cactus = Plant("Cactus", 5, 90, 0.8)
    sunflower = Plant("Sunflower", 5, 90, 0.8)
    fern = Plant("fern", 15, 120, 0.8)
