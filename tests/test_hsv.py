"""Tests HSV color interpolation."""

import unittest as ut
from src.color_lerp.hsv import interpolate_hsv


class TestHSV(ut.TestCase):
    """Tests HSV color interpolation."""

    def test_one_step(self):
        """Tests one step of HSV interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)
        actual = interpolate_hsv(color_start, color_end, 1)
        expected = [(0, 255, 0)]
        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_two_steps(self):
        """Tests two steps of HSV interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 255, 0)
        actual = interpolate_hsv(color_start, color_end, 2)
        expected = [(255, 0, 0), (0, 255, 0)]
        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_three_steps(self):
        """Tests three steps of HSV interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)
        actual = interpolate_hsv(color_start, color_end, 3)
        expected = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_four_steps(self):
        """Tests four steps of HSV interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)
        actual = interpolate_hsv(color_start, color_end, 4)
        expected = [(255, 0, 0), (170, 255, 0), (0, 255, 169), (0, 0, 255)]
        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)


if __name__ == '__main__':
    ut.main()
