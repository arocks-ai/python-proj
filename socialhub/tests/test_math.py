def sum(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


class Test_math:

    def test_sum(self):
        assert sum(2, 3) == 5
        assert sum(-1, 1) == 0
        assert sum(0, 0) == 0


    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 0) == 0
        assert subtract(-1, -1) == 0