from package_module_b.substract import substract_one, substract_two, substract_zero


def test_substract_one():
    assert substract_one(0) == -1
    assert substract_one(1) == 0
    assert substract_one(2) == 1


def test_substract_two():
    assert substract_two(0) == -2
    assert substract_two(1) == -1
    assert substract_two(2) == 0


def test_substract_zero():
    assert substract_zero(0) == 0
    assert substract_zero(1) == 1
    assert substract_zero(2) == 2
