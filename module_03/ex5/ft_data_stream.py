import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["climb", "inspect", "grab", "move",
               "release", "run", "use", "swim"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(stream: list[tuple[str, str]]) -> \
                  Generator[list[tuple[str, str]], None, None]:
    while len(stream) > 0:
        i = random.randint(0, len(stream) - 1)
        print(f"Got event from list: {stream[i]}")
        del stream[i]
        yield stream


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream = gen_event()
    for event in range(1000):
        player, action = next(stream)
        print(f"Event {event}: Player {player} did action {action}")

    stream_list = [next(stream) for event in range(10)]
    print(f"Built list of 10 event: {stream_list}")

    for _ in consume_event(stream_list):
        print(f"Remains in list: {stream_list}")
