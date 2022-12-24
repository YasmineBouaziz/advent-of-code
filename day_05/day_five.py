from collections import defaultdict
from collections import deque
import re

# part one
def move_crates(crate_dict, command_str: str):
    amount, from_, to = parse_str(command_str)
    while amount > 0:
        moved_crate = crate_dict[from_].pop()
        crate_dict[to].append(moved_crate)
        amount -= 1


# part 2
def move_crates_part2(crate_dict, command_str: str):
    amount, from_, to = parse_str(command_str)
    crates = []
    while amount > 0:
        crates.append(crate_dict[from_].pop())
        amount -= 1

    while crates:
        crate_dict[to].append(crates.pop())


def parse_str(command_str: str):
    split_str = command_str.split(" ")
    return int(split_str[1]), int(split_str[3]), int(split_str[5])


def part_one():
    with open("day_5_input.txt") as f:
        lines = f.readlines()
        # Each line is of length 36
        # A stack takes up 3 spaces then is succeeded by a space
        # Except for the final and first stack
        # E.g. '[G] [G] [C] [J] [P] [P] [Z] [R] [H]\n'
        # 2 chars are the new line so the length is 34
        # '[G] [G] [C] [J] [P] [P] [Z] [R] [H]'
        # We can determine by elements which stack they belong on
        # We have 9 stacks
        # [0:3] is a stack (doesn't include last element)
        # Then [4:7]
        # So + 4 and iterate through
        # '    [G] [C] [J] [P] [P] [Z] [R] [H]'
        stacks = defaultdict(deque)
        seen_blank = False
        for line in lines:
            if len(line) > 1 and line[1] == "1":
                seen_blank = True
            line = line.replace("\n", "")
            stack_start = 0
            stack_end = 3
            curr_stack = 1
            if not seen_blank:
                while stack_end <= len(line):
                    if not line[stack_start:stack_end].isspace():
                        stacks[curr_stack].appendleft(line[stack_start:stack_end])
                        curr_stack += 1
                        stack_start += 4
                        stack_end += 4
                    else:
                        curr_stack += 1
                        stack_start += 4
                        stack_end += 4
            elif len(line) > 1 and line[1] != "1":
                move_crates(stacks, line)

    ans = []
    for stack_key, stack in stacks.items():
        ans.append((stack_key, stack[-1]))
    answer = "".join([x[1] for x in sorted(ans)])
    answer = re.sub(r"[\([{})\]]", "", answer)
    return f"The answer for part one is: {answer}"


def part_two():
    with open("day_5_input.txt") as f:
        lines = f.readlines()
        stacks = defaultdict(deque)
        seen_blank = False
        for line in lines:
            if len(line) > 1 and line[1] == "1":
                seen_blank = True
            line = line.replace("\n", "")
            stack_start = 0
            stack_end = 3
            curr_stack = 1
            if not seen_blank:
                while stack_end <= len(line):
                    if not line[stack_start:stack_end].isspace():
                        stacks[curr_stack].appendleft(line[stack_start:stack_end])
                        curr_stack += 1
                        stack_start += 4
                        stack_end += 4
                    else:
                        curr_stack += 1
                        stack_start += 4
                        stack_end += 4
            elif len(line) > 1 and line[1] != "1":
                move_crates_part2(stacks, line)

    ans = []
    for stack_key, stack in stacks.items():
        ans.append((stack_key, stack[-1]))
    answer = "".join([x[1] for x in sorted(ans)])
    answer = re.sub(r"[\([{})\]]", "", answer)
    return f"The answer for par two is: {answer}"


print(part_one())
print(part_two())
