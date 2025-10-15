from unittest import TestCase

from day2.main import is_safe, is_safe_damp, parse_line


class Test(TestCase):
    def test_parse_line(self):
        if parse_line("1 3 6 7 9") != [1, 3, 6, 7, 9]:
            self.fail()

    def test_is_safe(self):
        if not is_safe([7, 6, 4, 2, 1]):
            self.fail()
        if is_safe([1, 2, 7, 8, 9]):
            self.fail()
        if not is_safe([1, 3, 6, 7, 9]):
            self.fail()

    def test_is_safe_damp(self):
        cases = [
            [[7, 6, 4, 2, 1], True],
            [[1, 2, 7, 8, 9], False],
            [[9, 7, 6, 2, 1], False],
            [[1, 3, 2, 4, 5], True],
            [[8, 6, 4, 4, 1], True],
            [[1, 3, 6, 7, 9], True]
        ]
        for case in cases:
            if is_safe_damp(case[0]) != case[1]:
                self.fail(msg=f"failed case {case[0]}: expected {case[1]}, got {is_safe_damp(case[0])}")
