from main import sum


def test_sum_positive():
    assert sum(10, 20) == 30


def test_sum_negative():
    assert sum(-5, -3) == -8


def test_sum_zero():
    assert sum(0, 5) == 5
