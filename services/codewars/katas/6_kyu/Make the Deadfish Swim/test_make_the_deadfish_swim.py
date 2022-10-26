from solution_make_the_deadfish_swim import parse


def test_parse():
    assert parse("ooo") == [0,0,0]
    assert parse("ioioio") == [1,2,3]
    assert parse("idoiido") == [0,1]
    assert parse("isoisoiso") == [1,4,25]
    assert parse("codewars") == [0]
    assert parse("zxczxczxczxczxczxczxc") == []