import random


def gen_player_achievements():
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

    random_achievs = []
    for achiv in range(random.randrange(len(achievements))):
        random_achievs.append(random.choice(achievements))
    return set(random_achievs)

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    player_alice = gen_player_achievements()
    print(f"Player Alice: {player_alice}")
    player_bob = gen_player_achievements()
    print(f"Player Bob: {player_bob}")
    player_charlie = gen_player_achievements()
    print(f"Player Charlie: {player_charlie}")
    player_dylan = gen_player_achievements()
    print(f"Player Dylan: {player_dylan}")
    print()
    
    print(f"All distinct achievements: {set.union(player_charlie, player_bob, player_charlie, player_dylan)}")
    print()

    print(f"Common achievements: {set.intersection(player_charlie, player_bob, player_charlie, player_dylan)}")
    print()

    print(f"Only Alice has: {set.difference(player_charlie, player_bob, player_charlie, player_dylan)}")
    print(f"Only Bob has: {set.difference(player_charlie, player_bob, player_charlie, player_dylan)}")
    print(f"Only Charlie has: {set.difference(player_charlie, player_bob, player_charlie, player_dylan)}")
    print(f"Only Dylan has: {set.difference(player_charlie, player_bob, player_charlie, player_dylan)}")
