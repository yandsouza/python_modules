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
        if isinstance(data, (int, float)):
            return True
        else:
            for value in data:
                if isinstance(value, (int, float)):
                    return True
                else:
                    return False
        return False

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
        if isinstance(data, str):
            return True
        else:
            for value in data:
                if isinstance(value, str):
                    return True
                else:
                    return False
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Incorrect text data")
        if isinstance(data, str):
            self.store_data(data)
        else:
            for value in data:
                self.store_data(value)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        else:
            for value in data:
                if isinstance(value, dict):
                    return True
                else:
                    return False
        return False

    def log_format(self, log: dict[str, str]) -> str:
        level = log["log_level"]
        msg = log["log_message"]
        return f"{level}: {msg}"

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Incorrect text data")
        if isinstance(data, dict):
            self.store_data(self.log_format(data))
        else:
            for value in data:
                self.store_data(self.log_format(value))


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
        print(f" Numeric value {rank}: {value}")
    print()

    data_str = TextProcessor()
    print("Testing Text Processor...")
    print(" Trying to validate input 'Hello':",
          data_str.validate("Hello"))
    print(" Trying to validate input '42':",
          data_str.validate(42))

    list_str = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {list_str}")
    for text in list_str:
        data_str.ingest(text)

    print(" Extracting 1 values...")
    for _ in range(1):
        rank, value = data_str.output()
        print(f" Text value {rank}: {value}")
    print()

    data_log = LogProcessor()
    print("Testing Log Processor...")
    print(" Trying to validate input '{'Key': 'Value'}':",
          data_log.validate({"Key": "Value"}))
    print(" Trying to validate input 'Hello':",
          data_log.validate("Hello"))

    list_log = [{"log_level": "NOTICE", "log_message": "Connection to server"},
                {"log_level": "ERROR", "log_message": "Unauthorized access!!"}]
    print(f" Processing data: {list_log}")
    for log in list_log:
        data_log.ingest(log)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = data_log.output()
        print(f" Log entry {rank}: {value}")
