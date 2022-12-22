import string

with open("day_3_input.txt") as file:
    data = file.read().splitlines()

# creating priority ditionary
priority_lower = list(string.ascii_lowercase)
priority_upper = list(string.ascii_uppercase)

lower_dict = {}
upper_dict = {}

for (i, item) in enumerate(priority_lower, start=1):
    lower_dict[item] = i

for (i, item) in enumerate(priority_upper, start=27):
    upper_dict[item] = i

letter_dict = {**upper_dict, **lower_dict}

# matching to dictionaries
def part_one():
    sum = 0
    for d in data:
        first_part, second_part = d[: len(d) // 2], d[len(d) // 2 :]
        common = [match for match in first_part if match in second_part][0]
        sum += letter_dict[common]
    return sum


def part_two():
    sum = 0
    count = 0
    elf_group = []
    for d in data:
        count += 1
        if count >= 3:
            common = [
                match for match in elf_group[0] if match in elf_group[1] and match in d
            ][0]
            sum += letter_dict[common]
            count = 0
            elf_group = []
        else:
            elf_group.append(d)
    return sum


print(f"The solution for part one is: {part_one()}")
print(f"The solution for part two is: {part_two()}")
