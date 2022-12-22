with open("day_4_input.txt") as file:
    data = file.read().splitlines()

count = 0
c = 0
for d in data:
    chunk_a, chunk_b = d.split(",")

    double_a, triple_a = [int(num) for num in chunk_a.split("-")]
    double_b, triple_b = [int(num) for num in chunk_b.split("-")]

    if (
        double_a <= double_b
        and triple_a >= triple_b
        or double_b <= double_a
        and triple_b >= triple_a
    ):
        count += 1

    if triple_b >= double_a >= double_b or triple_a >= double_b >= double_a:
        c += 1

print(f"result for part one is: {count}")
print(f"result for part two is: {c}")
