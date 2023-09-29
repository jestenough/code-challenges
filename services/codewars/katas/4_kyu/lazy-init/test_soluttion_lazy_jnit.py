from solution_lazy_init import LazyInit


def test_lazy_init():
    class Person(metaclass=LazyInit):
        def __init__(self, name, age): pass

    class Circle(metaclass=LazyInit):
        def __init__(self, x, y, ray): pass

    a_person = Person('Luke', 21)

    assert a_person.name == 'Luke'
    assert a_person.age == 21

    a_circle = Circle(0, 0, 5)
    assert a_circle.x == 0
    assert a_circle.y == 0
    assert a_circle.ray == 5

    class Car(metaclass=LazyInit):
        def __init__(self, model, color, plate, year): pass

    class Nothing(metaclass=LazyInit):
        def __init__(self, nothing): pass

    a_car = Car('Ford Ka', 'Blue', 'AF329SZ', 1999)
    a_nothing = Nothing('nothing')

    assert a_car.model == 'Ford Ka'
    assert a_car.color == 'Blue'
    assert a_car.plate == 'AF329SZ'
    assert a_car.year == 1999
    assert a_nothing.nothing == 'nothing'
