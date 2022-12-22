with open("day_2_input.txt") as file:
    data = file.read().splitlines()

input_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

new_input_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

points_per_shape = {"rock": 1, "paper": 2, "scissors": 3}
points_per_outcome = {"lose": 0, "draw": 3, "win": 6}


def round_1():
    draw = 0
    lose = 0
    win = 0
    for d in data:
        string = d.split()
        opps_shape = input_map[string[0]]
        our_shape = input_map[string[1]]

        if opps_shape == our_shape:
            draw += points_per_outcome["draw"] + points_per_shape[our_shape]
        elif (opps_shape, our_shape) in [
            ("paper", "rock"),
            ("rock", "scissors"),
            ("scissors", "paper"),
        ]:
            lose += points_per_outcome["lose"] + points_per_shape[our_shape]
        else:
            win += points_per_outcome["win"] + points_per_shape[our_shape]

    part_one_solution = draw + lose + win
    return part_one_solution


def round_2():
    draw = 0
    lose = 0
    win = 0
    for d in data:
        string = d.split()
        opps_shape = new_input_map[string[0]]
        our_shape = new_input_map[string[1]]

        if (opps_shape, our_shape) in [
            ("rock", "draw"),
            ("paper", "lose"),
            ("scissors", "win"),
        ]:
            draw += points_per_outcome[our_shape] + points_per_shape["rock"]
        elif (opps_shape, our_shape) in [
            ("rock", "win"),
            ("paper", "draw"),
            ("scissors", "lose"),
        ]:
            lose += points_per_outcome[our_shape] + points_per_shape["paper"]
        else:
            win += points_per_outcome[our_shape] + points_per_shape["scissors"]

    part_two_solution = draw + lose + win
    return part_two_solution


print(f"The solution for part one is: {round_1()}")
print(f"The solution for part two is: {round_2()}")
