from printingdepartment import compute_adjacency, load_data

data = load_data("test-input.txt")
# print(data)

assert compute_adjacency(data) == 13
