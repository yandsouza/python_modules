import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()

    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")

    capitalized_names = [name.capitalize() for name in players]
    print(f"New list of all names capitalized: {capitalized_names}")

    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized name only: {capitalized_only}")
    print()

    dict_scores = {names: random.randrange(0, 1000)
                   for names in capitalized_names}
    print(f"Score dict: {dict_scores}")

    average_score = round(sum(dict_scores.values())
                          / len(dict_scores.keys()), 2)
    print(f"Score average is: {average_score}")

    high_scores = {name: dict_scores[name] for name in dict_scores
                   if dict_scores[name] > average_score}
    print(f"High scores: {high_scores}")
