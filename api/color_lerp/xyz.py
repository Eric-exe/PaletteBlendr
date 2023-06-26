"""Color interpolation using XYZ color space."""

from colormath.color_objects import XYZColor, sRGBColor
from colormath.color_conversions import convert_color


def interpolate_xyz_percentage(color_start, color_end, percentage):
    """Takes two XYZ colors and a percentage, returns an RGB color."""

    x_begin = color_start.xyz_x
    x_end = color_end.xyz_x
    y_begin = color_start.xyz_y
    y_end = color_end.xyz_y
    z_begin = color_start.xyz_z
    z_end = color_end.xyz_z

    new_x = x_begin + (x_end - x_begin) * percentage
    new_y = y_begin + (y_end - y_begin) * percentage
    new_z = z_begin + (z_end - z_begin) * percentage

    # convert back to RGB
    xyz = XYZColor(new_x, new_y, new_z)
    rgb = convert_color(xyz, sRGBColor)

    # scale and round RGB values to the 0-255 range
    red = int(max(0, min(rgb.rgb_r * 255, 255)))
    green = int(max(0, min(rgb.rgb_g * 255, 255)))
    blue = int(max(0, min(rgb.rgb_b * 255, 255)))

    return (red, green, blue)


def interpolate_xyz(color_start, color_end, steps):
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

    # convert to XYZ
    xyz_start = convert_color(color_start, XYZColor)
    xyz_end = convert_color(color_end, XYZColor)

    # edge case, steps = 1
    if steps == 1:
        return [interpolate_xyz_percentage(xyz_start, xyz_end, 0.5)]

    # interpolate
    colors = []
    percent_step = 1 / (steps - 1)
    current_percent = 0

    for _ in range(steps):
        colors.append(interpolate_xyz_percentage(
            xyz_start, xyz_end, current_percent))
        current_percent += percent_step

    # rounding errors, replace first and last colors with originals
    colors[0] = (color_start.rgb_r * 255, color_start.rgb_g *
                 255, color_start.rgb_b * 255)
    colors[-1] = (color_end.rgb_r * 255, color_end.rgb_g *
                  255, color_end.rgb_b * 255)

    return colors
