from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join([item for _, item in data]))


class JSONPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_output = ", ".join([f"\"item_{rank}\": "
                                f"\"{item}\"" for rank, item in data])
        print("{" + json_output + "}")


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            ingested = False
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    ingested = True
                    break
                if ingested is False:
                    print(f"{type(proc).__name__} DataStream error - Can't "
                          f"process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        for proc in self.processors:
            print(f"{type(proc).__name__}: total {proc.rank} items processed, "
                  f"remaining {len(proc.memory)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            output_list: list[tuple[int, str]] = []
            output_list = [proc.output() for _ in range(nb)
                           if len(proc.memory) > 0]
            plugin.process_output(output_list)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print()

    print("Initialize Data Stream...")
    stream = DataStream()

    stream.print_processors_stats()
    print()

    print("Registering Processors")
    print()
    data_int = NumericProcessor()
    data_str = TextProcessor()
    data_log = LogProcessor()
    stream.register_processor(data_int)
    stream.register_processor(data_str)
    stream.register_processor(data_log)

    data_list = ["Hello world", [3.14, -1, 2.71],
                 [{"log_level": "WARNING", "log_message":
                  "Telnet access! Use ssh instead"},
                  {"log_level": "INFO", "log_message":
                   "User wil isconnected"}], 42,
                 ["Hi", "five"]]
    print("Send first batch of data on stream:", data_list)
    print()

    stream.process_stream(data_list)
    print()

    stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    print()

    stream.print_processors_stats()
    print()

    data_list_2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                   [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                    {'log_level': 'NOTICE', 'log_message':
                    'Certificate expires in 10 days'}],
                   [32, 42, 64, 84, 128, 168], 'World hello']
    print("Send another batch of data:", data_list_2)
    print()

    stream.process_stream(data_list_2)
    print()

    stream.print_processors_stats()
    print()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())
    print()

    stream.print_processors_stats()
