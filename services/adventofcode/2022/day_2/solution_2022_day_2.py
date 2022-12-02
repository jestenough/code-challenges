def day_2_two_parts():
    scores = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    values = {
        "A": "rock",
        "X": "rock",
        "B": "paper",
        "Y": "paper",
        "C": "scissors",
        "Z": "scissors",
    }

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    part_two_condition = {
        "X": "loss",
        "Y": "draw",
        "Z": "win",
    }

    round_result = {
        "loss": 0,
        "win": 6,
        "draw": 3,
    }

    import os
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        rounds = file.readlines()

    part1_total_score = 0
    part2_total_score = 0
    for _round in rounds:
        _round = _round.strip()
        opponent_value, my_value = _round.split(" ")

        if values[opponent_value] == values[my_value]:
            part1_total_score += round_result["draw"] + scores[values[my_value]]
        elif values[opponent_value] == beats[values[my_value]]:
            part1_total_score += round_result["win"] + scores[values[my_value]]
        else:
            part1_total_score += round_result["loss"] + scores[values[my_value]]

        if part_two_condition[my_value] == "draw":
            part2_total_score += round_result[part_two_condition[my_value]] + scores[values[opponent_value]]
        elif part_two_condition[my_value] == "loss":
            part2_total_score += round_result[part_two_condition[my_value]] + scores[beats[values[opponent_value]]]
        elif part_two_condition[my_value] == "win":
            part2_total_score += round_result[part_two_condition[my_value]] + scores[{v: k for k, v in beats.items()}[values[opponent_value]]]
    else:
        return [part1_total_score, part2_total_score]
