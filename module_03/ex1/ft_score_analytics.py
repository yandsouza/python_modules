import sys

def ft_score_analytics() -> None:
    try:
        for arg in sys.argv[1:]:
            int(arg)
    except ValueError as error:
        for arg in sys.argv[1:]:
            print(f"Invalid parameter: {arg}")
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    if len(sys.argv) == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    scores = [int(num) for num in sys.argv[1:]]
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
