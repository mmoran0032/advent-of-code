from pathlib import Path


def update_dial(current_dial: int, change: str) -> tuple[int, int]:
    zero_crossings = 0
    updated_dial = current_dial

    direction, steps = change[0], int(change[1:])

    if direction == "L":
        steps *= -1

    updated_dial = current_dial + steps

    while updated_dial > 99:  # from turning right
        updated_dial -= 100
        zero_crossings += 1
    while updated_dial < 0:  # from turning left
        updated_dial += 100
        zero_crossings += 1

    # we overcount when turning left and starting on zero
    if direction == "L" and current_dial == 0:
        zero_crossings = max(0, zero_crossings - 1)
    # we undercount when turning left and landing on zero
    if direction == "L" and updated_dial == 0:
        zero_crossings += 1

    return updated_dial, zero_crossings


def part_one(data: list[str]) -> int:
    num_zeros = 0
    dial_position = 50

    for change in data:
        dial_position, _ = update_dial(dial_position, change)
        if dial_position == 0:
            num_zeros += 1

    return num_zeros


def part_two(data: list[str]) -> int:
    num_zeros = 0
    dial_position = 50

    # print("START", dial_position, num_zeros)

    for change in data:
        new_position, zero_crossings = update_dial(dial_position, change)
        num_zeros += zero_crossings

        # print(dial_position, f"-> {change} ->", new_position, zero_crossings, num_zeros)
        dial_position = new_position

    return num_zeros


if __name__ == "__main__":
    data = Path("full-input.txt").read_text().strip().split()
    print(part_one(data))
    print(part_two(data))
