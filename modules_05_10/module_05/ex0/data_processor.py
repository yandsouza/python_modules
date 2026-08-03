from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.memory: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def store_data(self, data: str) -> None:
        self.memory.append((self.rank, data))
        self.rank += 1

    def output(self) -> tuple[int, str]:
        return self.memory.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Incorrect numeric data")
        if isinstance(data, (int, float)):
            self.store_data(str(data))
        else:
            for value in data:
                self.store_data(str(value))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Incorrect text data")
        if isinstance(data, str):
            self.store_data(data)
        else:
            for value in data:
                self.store_data(value)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print()

    data_int = NumericProcessor()
    print("Testing Numeric Processor...")
    print(" Trying to validate input '42':",
          data_int.validate(42))
    print(" Trying to validate input 'Hello':",
          data_int.validate("Hello"))

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        data_int.ingest("foo")
    except ValueError:
        print(" Got exception: Improper numeric data")

    nums = [1, 2, 3, 4, 5]
    print(f" Processing data: {nums}")
    for num in nums:
        data_int.ingest(num)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = data_int.output()
        print(f" Extracting value {rank}: {value}")
