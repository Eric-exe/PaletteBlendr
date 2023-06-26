"""Linearly interpolate between two RGB colors."""


def interpolate_rgb_percentage(color_start, color_end, percentage):
    """Linearly interpolate between two RGB colors."""

    red = color_start[0] + (color_end[0] - color_start[0]) * percentage
    green = color_start[1] + (color_end[1] - color_start[1]) * percentage
    blue = color_start[2] + (color_end[2] - color_start[2]) * percentage

    # stay within 0-255 range, as an integer
    red = int(max(0, min(255, red)))
    green = int(max(0, min(255, green)))
    blue = int(max(0, min(255, blue)))

    return (red, green, blue)


def interpolate_rgb(color_start, color_end, steps):
    """Linearly interpolate between two RGB colors in steps."""

    # edge cases
    if steps == 1:
        # return the midpoint
        return [interpolate_rgb_percentage(color_start, color_end, 0.5)]
    elif steps == 2:
        # return the start and end
        return [color_start, color_end]

    colors = []
    percent_step = 1 / (steps - 1)
    current_percent = 0

    for _ in range(steps):
        colors.append(interpolate_rgb_percentage(
            color_start, color_end, current_percent))
        current_percent += percent_step

    # rounding errors, replace first and last colors with originals
    colors[0] = color_start
    colors[-1] = color_end

    return colors
