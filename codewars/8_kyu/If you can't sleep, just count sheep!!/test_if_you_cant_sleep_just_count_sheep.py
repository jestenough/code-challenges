from solution_if_you_cant_sleep_just_count_sheep import count_sheep


def test_count_sheep():
    assert(count_sheep(0) == "");
    assert(count_sheep(1) == "1 sheep...");
    assert(count_sheep(2) == "1 sheep...2 sheep...")
    assert(count_sheep(3) == "1 sheep...2 sheep...3 sheep...")
