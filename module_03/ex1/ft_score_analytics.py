import sys

def validade_list(arg):
    try:
        int(arg)
    except ValueError as error:
        print(f"Invalid parameter: {arg}")
    else:
        return int(arg)

def print_score(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")

def ft_score_analytics() -> None:
    scores = []
    for arg in sys.argv[1:]:
        value = validade_list(arg)
        if value is not str and value is not None:
            scores.append(value)
    if not scores:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return 
    print_score(scores)

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
