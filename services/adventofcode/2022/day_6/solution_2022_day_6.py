def day_6_two_parts():
    import os
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
        datastream_buffer = file.read()
    
    part_one_marker, part_one_chr_to_start = 4, 0
    part_two_marker, part_two_chr_to_start = 14, 0
    found_part_one, found_part_two = False, False

    for index, value in enumerate(datastream_buffer):
        if len(set(datastream_buffer[index:index+part_one_marker])) == part_one_marker and not found_part_one:
            part_one_chr_to_start, found_part_one = index+part_one_marker, True
        if len(set(datastream_buffer[index:index+part_two_marker])) == part_two_marker and not found_part_two:
            part_two_chr_to_start, found_part_two = index+part_two_marker, True
    
    return [part_one_chr_to_start, part_two_chr_to_start]