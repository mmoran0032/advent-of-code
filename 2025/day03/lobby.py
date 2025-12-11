from pathlib import Path
from typing import Callable


def find_max_joltage(bank: str) -> int:
    unique_joltages = set(
        int(f"{bank[i]}{bank[j]}") for i in range(0, len(bank)) for j in range(i + 1, len(bank))
    )

    # print(unique_joltages)

    return max(unique_joltages)


def find_max_joltage_long(bank: str) -> int:
    return 0


def driver(data: list[str], function: Callable) -> int:
    total_joltage = 0
    for bank in data:
        total_joltage += function(bank)

    return total_joltage


if __name__ == "__main__":
    data = Path("full-input.txt").read_text().strip().split()
    print(driver(data, find_max_joltage))
    print(driver(data, find_max_joltage_long))
