from package_module_c import fibo


def test_fibo_zero():
    assert fibo(0) == 1


def test_fibo_one():
    assert fibo(1) == 1


def test_fibo_two():
    assert fibo(2) == 2


def test_fibo_ten():
    assert fibo(10) == 89


def test_fibo_twenty():
    assert fibo(20) == 10946
