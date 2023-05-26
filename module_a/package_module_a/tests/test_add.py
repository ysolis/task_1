from package_module_a.add import add_one, add_two, add_zero


def test_add_one():
    assert add_one(0) == 1
    assert add_one(1) == 2
    assert add_one(2) == 3


def test_add_two():
    assert add_two(0) == 2
    assert add_two(1) == 3
    assert add_two(2) == 4


def test_add_zero():
    assert add_zero(0) == 0
    assert add_zero(1) == 1
    assert add_zero(2) == 2


def test_add_fail():
    assert add_two(5) == 7
