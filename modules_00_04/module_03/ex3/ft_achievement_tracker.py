import random


def gen_player_achievements() -> set[str]:
    achievements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Hidden Path Finder",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer"]

    random_num = random.randrange(1, len(achievements) + 1)
    return set(random.sample(achievements, random_num))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    players = [gen_player_achievements() for player in "0123"]

    print(f"Player Alice: {players[0]}")
    print(f"Player Bob: {players[1]}")
    print(f"Player Charlie: {players[2]}")
    print(f"Player Dylan: {players[3]}")
    print()

    all_achievements = set.union(*players)
    print(f"All distinct achievements: {all_achievements}")
    print()

    print(f"Common achievements: {set.intersection(*players)}")
    print()

    others_alice = set.union(players[1], players[2], players[3])
    others_bob = set.union(players[0], players[2], players[3])
    others_charlie = set.union(players[0], players[1], players[3])
    others_dylan = set.union(players[0], players[1], players[2])
    print(f"Only Alice has: "
          f"{set.difference(players[0], others_alice)}")
    print(f"Only Bob has: "
          f"{set.difference(players[1], others_bob)}")
    print(f"Only Charlie has: "
          f"{set.difference(players[2], others_charlie)}")
    print(f"Only Dylan has: "
          f"{set.difference(players[3], others_dylan)}")
    print()

    print(f"Alice is missing: "
          f"{set.difference(all_achievements, players[0])}")
    print(f"Bob is missing: "
          f"{set.difference(all_achievements, players[1])}")
    print(f"Charlie is missing: "
          f"{set.difference(all_achievements, players[2])}")
    print(f"Dylan is missing: "
          f"{set.difference(all_achievements, players[3])}")
    print()
