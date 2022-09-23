def high_and_low(numbers):
    integers_list = [int(i) for i in numbers.split()]
    return "{0} {1}".format(max(integers_list), min(integers_list))
