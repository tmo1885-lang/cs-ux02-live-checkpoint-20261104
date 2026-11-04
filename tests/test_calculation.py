from src.calculation import total, discounted_total

def test_total():
    assert total([2, 3]) == 5

def test_discounted_total():
    assert discounted_total([2, 3], 0.2) == 4
