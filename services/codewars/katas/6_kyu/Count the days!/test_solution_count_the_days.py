import datetime

from solution_count_the_days import count_days


def test_to_camel_case():
    d = datetime.datetime(2016, 12, 24, 18, 0)
    assert count_days(d) == "The day is in the past!"
