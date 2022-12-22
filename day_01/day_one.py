with open("day_1_input.txt") as file:
    data = file.read().splitlines()

max = 0
max2 = 0
max3 = 0
count = 0
for item in data:
    if item == "":
        count = 0
    else:
        num = int(item)
        count += num

    if count > max:
        max3 = max2
        max2 = max
        max = count
    elif count > max2:
        max3 = max2
        max2 = count
    elif count > max3:
        max3 = count

answer2 = max + max2 + max3

print(f"answer to part 1: {max}")
print(f"answer to part 2: {answer2}")
