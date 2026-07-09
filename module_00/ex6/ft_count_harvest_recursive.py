def ft_count_harvest_recursive():
    def count(days, i):
        print(f"Day {i}")
        if (i < days):
            count(days, i + 1)
    days = int(input("Days until harvest: "))
    count(days, 1)
    print("Harvest time!")
