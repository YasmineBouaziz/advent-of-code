with open("day_6_input.txt") as f:
    data = f.readline().strip()


def solution_one():
    for i in range(len(data)):
        if len(set(data[i : i + 4])) == 4:
            return i + 4


def solution_two():
    for i in range(len(data)):
        if len(set(data[i : i + 14])) == 14:
            return i + 14


print(solution_one())
print(solution_two())
