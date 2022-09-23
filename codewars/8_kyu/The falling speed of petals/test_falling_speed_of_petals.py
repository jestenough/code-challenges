from solution_the_falling_speed_of_petals import sakura_fall


def test_sakura_fall():
    assert(sakura_fall(5) == 80)
    assert(sakura_fall(10) == 40)
    assert(sakura_fall(-1) == 0)
