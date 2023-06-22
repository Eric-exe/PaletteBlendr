"""Test color interpolation in the XYZ color space."""

import unittest as ut
from src.color_lerp.xyz import interpolate_xyz


class TestXYZ(ut.TestCase):
    """Test color interpolation in the XYZ color space."""

    def test_one_step(self):
        """Tests one step of XYZ interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_xyz(color_start, color_end, 1)
        expected = [(180, 0, 213)]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_two_steps(self):
        """Tests two steps of XYZ interpolation, should return the same colors."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_xyz(color_start, color_end, 2)
        expected = [color_start, color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_three_steps(self):
        """Tests three steps of XYZ interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_xyz(color_start, color_end, 3)
        expected = [color_start, (180, 0, 213), color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)

    def test_four_steps(self):
        """Tests four steps of XYZ interpolation."""

        color_start = (255, 0, 0)
        color_end = (0, 0, 255)

        actual = interpolate_xyz(color_start, color_end, 4)
        expected = [color_start, (206, 2, 178), (149, 0, 242), color_end]

        assert actual == expected, f"Expected: {0}\nActual: {1}".format(
            expected, actual)


if __name__ == "__main__":
    ut.main()
