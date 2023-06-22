"""Tests RGB color interpolation."""

import unittest as ut
from src.color_lerp.rgb import interpolate_rgb


class TestRGB(ut.TestCase):
    """Tests RGB color interpolation."""

    def test_one_step(self):
        """Tests one step of RGB interpolation."""
        color_start = (255, 0, 0)
        color_end = (0, 255, 0)
        actual = interpolate_rgb(color_start, color_end, 1)
        expected = [(127, 127, 0)]
        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_two_steps(self):
        """Tests two steps of RGB interpolation."""
        color_start = (255, 0, 0)
        color_end = (0, 255, 0)
        actual = interpolate_rgb(color_start, color_end, 2)
        expected = [(255, 0, 0), (0, 255, 0)]
        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_three_steps(self):
        """Tests three steps of RGB interpolation."""
        color_start = (255, 0, 0)
        color_end = (0, 255, 0)
        actual = interpolate_rgb(color_start, color_end, 3)
        expected = [(255, 0, 0), (127, 127, 0), (0, 255, 0)]
        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_four_steps(self):
        """Tests four steps of RGB interpolation."""
        color_start = (255, 127, 63)
        color_end = (0, 255, 127)
        actual = interpolate_rgb(color_start, color_end, 4)
        expected = [(255, 127, 63), (170, 169, 84),
                    (85, 212, 105), (0, 255, 127)]
        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)


if __name__ == '__main__':
    ut.main()
