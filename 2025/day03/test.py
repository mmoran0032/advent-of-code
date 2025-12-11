from pathlib import Path

from lobby import driver, find_max_joltage, find_max_joltage_long

test_data = Path("test-input.txt").read_text().strip().split()

assert find_max_joltage("987654321111111") == 98
assert find_max_joltage("811111111111119") == 89
assert find_max_joltage("234234234234278") == 78
assert find_max_joltage("818181911112111") == 92

assert driver(test_data, find_max_joltage) == 357

assert find_max_joltage_long("987654321111111") == 987654321111
assert find_max_joltage_long("811111111111119") == 811111111119
assert find_max_joltage_long("234234234234278") == 434234234278
assert find_max_joltage_long("818181911112111") == 888911112111

assert driver(test_data, find_max_joltage_long) == 3121910778619
