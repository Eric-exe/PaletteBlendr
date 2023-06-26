"""Color Interpolation using HSV color space."""

import colorsys


def interpolate_hsv_percentage(color_start, color_end, percentage):
    """Takes two HSV colors and a percentage, returns an RGB color."""

    hue_start = color_start[0]
    hue_end = color_end[0]

    # Calculate the shortest distance between hue values
    hue_dist = min((hue_end - hue_start) % 1, (hue_start - hue_end) % 1)
    if hue_dist > 0.5:
        # Adjust for wraparound when the shortest distance exceeds 0.5
        if hue_end > hue_start:
            hue_end -= 1
        else:
            hue_start -= 1

    # Interpolate hue, saturation, and value components
    hue = hue_start + (hue_end - hue_start) * percentage
    saturation = color_start[1] + (color_end[1] - color_start[1]) * percentage
    value = color_start[2] + (color_end[2] - color_start[2]) * percentage

    # Convert back to RGB
    rgb = colorsys.hsv_to_rgb(hue % 1, saturation, value)

    # Scale and round RGB values to the 0-255 range
    red = int(max(0, min(rgb[0] * 255, 255)))
    green = int(max(0, min(rgb[1] * 255, 255)))
    blue = int(max(0, min(rgb[2] * 255, 255)))

    return (red, green, blue)


def interpolate_hsv(color_start, color_end, steps):
    """Takes two RGB colors and the number of steps, returns a list of RGB colors."""

    # convert to HSV, and normalize
    hsv_start = colorsys.rgb_to_hsv(color_start[0] / 255,
                                    color_start[1] / 255,
                                    color_start[2] / 255)

    hsv_end = colorsys.rgb_to_hsv(color_end[0] / 255,
                                  color_end[1] / 255,
                                  color_end[2] / 255)

    # edge cases
    if steps == 1:
        # return the midpoint
        return [interpolate_hsv_percentage(hsv_start, hsv_end, 0.5)]
    elif steps == 2:
        # return the start and end
        return [color_start, color_end]

    # interpolate
    colors = []
    percent_step = 1 / (steps - 1)
    current_percent = 0

    for _ in range(steps):
        colors.append(interpolate_hsv_percentage(
            hsv_start, hsv_end, current_percent))
        current_percent += percent_step

    # rounding errors, replace first and last colors with originals
    colors[0] = color_start
    colors[-1] = color_end

    return colors
