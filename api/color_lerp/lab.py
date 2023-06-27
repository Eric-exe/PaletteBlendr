"""Interpolation functions for the LAB color space."""

from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color


def interpolate_lab_percentage(color_start, color_end, percentage):
    """Takes two RGB colors and a percentage, returns an RGB color."""

    l_start = color_start.lab_l
    l_end = color_end.lab_l
    a_start = color_start.lab_a
    a_end = color_end.lab_a
    b_start = color_start.lab_b
    b_end = color_end.lab_b

    new_l = l_start + (l_end - l_start) * percentage
    new_a = a_start + (a_end - a_start) * percentage
    new_b = b_start + (b_end - b_start) * percentage

    # convert back to RGB
    lab = LabColor(new_l, new_a, new_b)

    rgb = convert_color(lab, sRGBColor)

    # scale and round RGB values to the 0-255 range
    red = int(max(0, min(rgb.rgb_r * 255, 255)))
    green = int(max(0, min(rgb.rgb_g * 255, 255)))
    blue = int(max(0, min(rgb.rgb_b * 255, 255)))

    return (red, green, blue)


def interpolate_lab(color_start, color_end, steps):
    """Takes two RGB colors and the number of steps, returns a list of RGB colors."""

    # edge case, steps = 2
    if steps == 2:
        return [color_start, color_end]

    color_start = sRGBColor(color_start[0] / 255,
                            color_start[1] / 255,
                            color_start[2] / 255)

    color_end = sRGBColor(color_end[0] / 255,
                          color_end[1] / 255,
                          color_end[2] / 255)

    # convert to LAB
    lab_start = convert_color(color_start, LabColor)
    lab_end = convert_color(color_end, LabColor)

    # edge case, steps = 1
    if steps == 1:
        return [interpolate_lab_percentage(lab_start, lab_end, 0.5)]

    # interpolate
    colors = []
    percent_step = 1 / (steps - 1)
    current_percent = 0

    for _ in range(steps):
        colors.append(interpolate_lab_percentage(
            lab_start, lab_end, current_percent))
        current_percent += percent_step

    # rounding errors, replace first and last colors with originals
    colors[0] = (int(color_start.rgb_r * 255),
                 int(color_start.rgb_g * 255),
                 int(color_start.rgb_b * 255))

    colors[-1] = (int(color_end.rgb_r * 255),
                  int(color_end.rgb_g * 255),
                  int(color_end.rgb_b * 255))


    return colors
