"""Tests LCHuv color interpolation."""

import unittest as ut
from src.color_lerp.lchuv import interpolate_lchuv


class TestLCHuv(ut.TestCase):
    """Tests LCHuv color interpolation."""

    def test_one_step(self):
        """Tests one step of LCHuv interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lchuv(color_start, color_end, 1)
        expected = [(232, 0, 216)]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_two_steps(self):
        """Tests two steps of LCHuv interpolation, should return the same colors."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lchuv(color_start, color_end, 2)
        expected = [color_start, color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_three_steps(self):
        """Tests three steps, should return beginning, middle, end"""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lchuv(color_start, color_end, 3)
        expected = [color_start, (232, 0, 216), color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_four_steps(self):
        """Tests four steps, should return beginning, middle, middle, end"""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lchuv(color_start, color_end, 4)
        expected = [color_start, (244, 0, 173), (206, 0, 249), color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)


if __name__ == '__main__':
    ut.main()
