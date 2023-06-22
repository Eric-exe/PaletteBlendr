"""Tests color interpolation in the LAB color space."""

import unittest as ut
from src.color_lerp.lab import interpolate_lab


class TestLAB(ut.TestCase):
    """Tests color interpolation in the LAB color space."""

    def test_one_step(self):
        """Tests one step of LAB interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lab(color_start, color_end, 1)
        expected = [(202, 0, 137)]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_two_steps(self):
        """Tests two steps of LAB interpolation, should return the same colors."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lab(color_start, color_end, 2)
        expected = [color_start, color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_three_steps(self):
        """Tests three steps of LAB interpolation"""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lab(color_start, color_end, 3)
        expected = [color_start, (202, 0, 137), color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_four_steps(self):
        """Tests four steps of LAB interpolation"""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_lab(color_start, color_end, 4)
        expected = [color_start, (220, 0, 99), (178, 0, 175), color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)


if __name__ == '__main__':
    ut.main()
