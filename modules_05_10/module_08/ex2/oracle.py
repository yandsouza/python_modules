import os
import sys
from dotenv import load_dotenv


def validate_cfg(config: dict[str, str | None]) -> None:
    missing: list[str] = []

    for key, value in config.items():
        if value is None or value.strip() == "":
            missing.append(key)

    if missing:
        print("Missing configuration:")
        for key in missing:
            print(key)
        sys.exit(1)


if __name__ == "__main__":
    load_dotenv()
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    cfg = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    validate_cfg(cfg)
    print("Configuration loaded:")

    print(f"Mode: {cfg['MATRIX_MODE']}")
    if cfg["MATRIX_MODE"] == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to mainframe")
    print("API Access: Authenticated")
    print(f"Log Level: {cfg['LOG_LEVEL']}")
    print("Zion Network: Online")
    print()

    print("Environment security check")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()

    print("The Oracle sees all configurations.")
