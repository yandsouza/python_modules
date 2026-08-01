from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self):
        print(self.data)


class NumericProcessor(DataProcessor):
    def __init__(self, data):
        self.data = data

    def validate(self, data: Any) -> bool:
        return isinstance(data, int)


class TextProcessor(DataProcessor):
    def __init__(self, data):
        self.data = data

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


if __name__ == "__main__":
    data_int = NumericProcessor(3)
    data_int_2 = NumericProcessor(5)
    data_str = TextProcessor("hello")
    data_int.output()
    data_int_2.output()
    data_str.output()
    print(data_int.validate("str"))
