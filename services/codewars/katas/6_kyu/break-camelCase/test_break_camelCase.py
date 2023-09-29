from solution_break_camelCase import solution


def test_solution():
    assert solution('helloWorld') == "hello World"
    assert solution("camelCase") == "camel Case"
    assert solution('breakCamelCase') == "break Camel Case"