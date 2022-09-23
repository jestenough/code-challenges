from solution_convert_pascalCase_string_into_snake_case import to_underscore


def test_to_underscore():
    assert(to_underscore("TestController") == "test_controller")
    assert(to_underscore("MoviesAndBooks") == "movies_and_books")
    assert(to_underscore("App7Test") == "app7_test")
    assert(to_underscore(1) == "1")
    assert(to_underscore(-125) == "-125")
