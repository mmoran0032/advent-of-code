from pathlib import Path

from secretentrance import part_one, part_two

test_data = Path("test-input.txt").read_text().strip().split()

assert part_one(test_data) == 3
assert part_two(test_data) == 6
