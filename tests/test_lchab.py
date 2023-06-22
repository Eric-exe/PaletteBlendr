"""Test cases for LCHab interpolation."""

import unittest as ut
from src.color_lerp.lchab import interpolate_lchab


class TestLCHab(ut.TestCase):
    """Test cases for LCHab interpolation."""

    def test_one_step(self):
        """Tests one step, should return middle value."""

        color_begin = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lchab(color_begin, color_end, 1)
        expected = [(249, 0, 129)]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_two_steps(self):
        """Tests two steps, should return the two colors."""

        color_begin = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lchab(color_begin, color_end, 2)
        expected = [color_begin, color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_three_steps(self):
        """Tests three steps, should return beginning, middle, and end colors"""

        color_begin = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lchab(color_begin, color_end, 3)
        expected = [color_begin, (249, 0, 129), color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_four_steps(self):
        """Tests for steps, should return beginning, two middle, and end colors"""

        color_begin = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lchab(color_begin, color_end, 4)
        expected = [color_begin, (255, 0, 89), (223, 0, 173), color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)


if __name__ == '__main__':
    ut.main()
