def day_1_two_parts():
    import os
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        x = f.read().split("\n\n")

    result = [sum((int(j) for j in i.split("\n") if j)) for i in x]

    return [max(result), sum(sorted(result, reverse=True)[:3])]