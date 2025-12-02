from functools import reduce
from pathlib import Path
from typing import Callable


def check_id_validity_simple(product_id: int) -> bool:
    pid = str(product_id)

    # odd-length ids must be valid
    if len(pid) % 2 != 0:
        return True

    front, back = pid[: len(pid) // 2], pid[len(pid) // 2 :]
    return front != back


def check_id_validity_advanced(product_id: int) -> bool:
    # we need to check if it's only repeated sequences of at least two
    pid = str(product_id)
    possible_lengths = range(1, len(pid) // 2 + 1)
    # print(pid, len(pid), len(pid) // 2 + 1)

    # for each length, see if the number of matched subsequences equals the entire length
    for length in possible_lengths:
        # print(length)
        substring = pid[:length]
        # print(pid, length, substring, pid.count(substring), len(pid), pid.count(substring) * length)
        if pid.count(substring) * length == len(pid):
            return False

    return True


def driver(data: list[str], valid_function: Callable) -> int:
    suspect_ids: list[int] = []  # so that I can spot-check

    for id_range in data:
        start, end = id_range.split("-")
        for i in range(int(start), int(end) + 1):
            if not valid_function(i):
                suspect_ids.append(i)

    # print(suspect_ids)
    return reduce(lambda x, y: x + y, suspect_ids, 0)


if __name__ == "__main__":
    data = Path("full-input.txt").read_text().strip().split(",")
    print(driver(data, check_id_validity_simple))
    print(driver(data, check_id_validity_advanced))
