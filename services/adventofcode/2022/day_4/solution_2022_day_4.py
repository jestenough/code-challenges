def day_4_two_parts():
    import os
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        list_of_pairs = file.readlines()
    
    assignment_pairs_bool = []
    assignment_pair_overlap_bool = []
    for pair in list_of_pairs:
        pure_pair = pair.rstrip()
        
        first_part_pair, second_part_pair = pure_pair.split(',')
        fir_split = first_part_pair.split('-')
        sec_split = second_part_pair.split('-')
        fir_list = set(range(int(fir_split[0]), int(fir_split[1])+1))
        sec_list = set(range(int(sec_split[0]), int(sec_split[1])+1))

        assignment_pairs_bool.append(any([fir_list.issubset(sec_list), sec_list.issubset(fir_list)]))
        assignment_pair_overlap_bool.append(bool(fir_list.intersection(sec_list)))

    return [sum(assignment_pairs_bool), sum(assignment_pair_overlap_bool)]
