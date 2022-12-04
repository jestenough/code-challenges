def day_3_two_parts():
    import os
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        rucksacks = file.readlines()

    abc_lower_upper = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))

    part_1_sum = 0
    part_2_sum = 0
    list_of_sets = []
    for iteration, rucksack in enumerate(rucksacks, start=1):
        pure_rucksack = rucksack.rstrip()

        list_of_sets.append(set(pure_rucksack))

        intersection_of_two_compartments = set(pure_rucksack[:len(pure_rucksack) // 2]).intersection(set(pure_rucksack[len(pure_rucksack) // 2:]))
        part_1_sum += sum([abc_lower_upper.index(character)+1 for character in intersection_of_two_compartments])

        if iteration % 3 == 0:
            part_2_sum += sum([abc_lower_upper.index(character)+1 for character in (set.intersection(*list_of_sets))])
            list_of_sets.clear()
    else:
        return [part_1_sum, part_2_sum]
