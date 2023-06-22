"""Interpolation functions for LCHab color space."""

from colormath.color_objects import LCHabColor, sRGBColor
from colormath.color_conversions import convert_color


def interpolate_lchab_percentage(color_start, color_end, percentage):
    """Takes two LCHab colors and a percentage, returns an RGB color."""

    l_start = color_start.lch_l
    l_end = color_end.lch_l

    c_start = color_start.lch_c
    c_end = color_end.lch_c

    h_start = color_start.lch_h
    h_end = color_end.lch_h

    new_l = l_start + (l_end - l_start) * percentage
    new_c = c_start + (c_end - c_start) * percentage

    # edge case, hue
    if abs(h_start - h_end) > 180:
        if h_start > h_end:
            h_start -= 360
        else:
            h_end -= 360

    new_h = h_start + (h_end - h_start) * percentage

    # convert back to RGB
    lchuv = LCHabColor(new_l, new_c, new_h)

    rgb = convert_color(lchuv, sRGBColor)

    # s scale and round RGB values to the 0-255 range
    red = int(max(0, min(rgb.rgb_r * 255, 255)))
    green = int(max(0, min(rgb.rgb_g * 255, 255)))
    blue = int(max(0, min(rgb.rgb_b * 255, 255)))

    return (red, green, blue)


def interpolate_lchab(color_start, color_end, steps):
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

    # convert to LCHuv
    lchuv_start = convert_color(color_start, LCHabColor)
    lchuv_end = convert_color(color_end, LCHabColor)

    # edge case, steps = 1
    if steps == 1:
        return [interpolate_lchab_percentage(lchuv_start, lchuv_end, 0.5)]

    # interpolate
    colors = []
    percent_step = 1 / (steps - 1)
    current_percent = 0

    for _ in range(steps):
        colors.append(interpolate_lchab_percentage(
            lchuv_start, lchuv_end, current_percent))
        current_percent += percent_step

    # rounding errors, replace first and last colors with originals
    colors[0] = (color_start.rgb_r * 255, color_start.rgb_g *
                 255, color_start.rgb_b * 255)
    colors[-1] = (color_end.rgb_r * 255, color_end.rgb_g *
                  255, color_end.rgb_b * 255)

    return colors
