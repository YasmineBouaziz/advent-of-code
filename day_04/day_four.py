with open("day_4_input.txt") as file:
    data = file.read().splitlines()

count = 0
c = 0
for d in data:
    chunk_a, chunk_b = d.split(",")

    aa, aaa = [int(num) for num in chunk_a.split("-")]
    bb, bbb = [int(num) for num in chunk_b.split("-")]

    if aa <= bb and aaa >= bbb or bb <= aa and bbb >= aaa:
        count += 1

    if bbb >= aa >= bb or aaa >= bb >= aa:
        c += 1

print(f"result for part one is: {count}")
print(f"result for part two is: {c}")
