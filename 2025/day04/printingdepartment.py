from pathlib import Path

import numpy as np


def load_data(filepath: Path | str) -> np.ndarray:
    if isinstance(filepath, str):
        filepath = Path(filepath)
    assert filepath.exists()
    data = filepath.read_text().strip().split()
    # we'll convert this into arrays of numbers
    mapping = {".": 0, "@": 1}
    processed = np.array([[mapping[char] for char in line] for line in data], dtype=np.int16)
    return processed


def compute_adjacency(data: np.ndarray) -> np.ndarray:
    # for each entry, we want to compute the number of rolls next to it
    # we can add buffer rows and columns, then sum the 8 adjacent cells
    padded = np.pad(data, 2)
    adjacent = (
        padded[:-2, :-2]
        + padded[:-2, 1:-1]
        + padded[:-2, 2:]
        + padded[1:-1, :-2]
        + padded[1:-1, 2:]
        + padded[2:, :-2]
        + padded[2:, 1:-1]
        + padded[2:, 2:]
    )[1:-1, 1:-1]
    # print(adjacent.shape, data.shape)
    # print(adjacent)
    assert adjacent.shape == data.shape

    # we want to see which roll locations have 3 or fewer adjacent
    masked = np.where(data, adjacent, -1)
    # print(masked)
    reachable = np.where((masked < 4) & (masked > -1), 1, 0)
    # print(reachable.sum())
    return reachable


def progressive_remove(data: np.ndarray) -> int:
    permuted_data = data
    to_remove = 0
    to_remove_step = -1
    steps = 0
    while to_remove_step != 0:
        reachable = compute_adjacency(permuted_data)
        to_remove_step = reachable.sum()
        to_remove += to_remove_step
        permuted_data -= reachable
        steps += 1

    return to_remove


if __name__ == "__main__":
    data = load_data("full-input.txt")
    print(compute_adjacency(data).sum())
    print(progressive_remove(data))
