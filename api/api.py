"""The main API for the flask project."""

from flask import Blueprint, request
from api.color_lerp import rgb, hsv, lchab, lchuv, lab, xyz
api_bp = Blueprint("api", __name__)

# =============================================================================
# Main function for the palette blender

def hex_to_rgb(hex_string):
    """Convert a hex color to RGB."""
    hex_string = hex_string.lstrip('#')
    return tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4))

def hex_list_to_rgb_list(hex_list):
    """Convert a list of hex colors to a list of RGB colors."""
    rgb_list = []
    for hex_string in hex_list:
        rgb_list.append(hex_to_rgb(hex_string))
    return rgb_list

def rgb_to_hex(rgb_tuple):
    """Convert an RGB color to hex."""
    return f'#%02x%02x%02x' % rgb_tuple

def rgb_list_to_hex_list(rgb_list):
    """Convert a list of RGB colors to a list of hex colors."""
    hex_list = []
    for rgb_tuple in rgb_list:
        hex_list.append(rgb_to_hex(rgb_tuple))
    return hex_list

def blend_palette_helper(funct, colors, steps, new_size):
    """The helper function for the palette blender."""

    steps += 2 # add the start and end colors
    new_colors = []
    for i in range(len(colors) - 1):
        new_colors.extend(funct(colors[i], colors[i + 1], steps))
        # remove the last color, since it's a duplicate

    # add the last color back in
    new_colors.append(colors[-1])

    res = []

    # calculate how many colors we need to skip
    skip = (len(new_colors) - 1) / (new_size - 1)

    # add the colors
    for i in range(new_size):
        res.append(new_colors[int(i * skip)])

    return rgb_list_to_hex_list(res)

def blend_palette(colors, new_size):
    """Blend the colors in the palette."""

    original_size = len(colors)

    # edge cases
    if original_size == 0 or new_size == 0:
        response = {
            'rgb': [],
            'hsv': [],
            'lchab': [],
            'lchuv': [],
            'lab': [],
            'xyz': []
        }

        return response
    
    if original_size == 1:
        response = {
            "rgb": [colors[0]] * new_size,
            "hsv": [colors[0]] * new_size,
            "lchab": [colors[0]] * new_size,
            "lchuv": [colors[0]] * new_size,
            "lab": [colors[0]] * new_size,
            "xyz": [colors[0]] * new_size
        }

        return response

    if new_size == 1:
        # special case, blend the first and last color
        begin = hex_to_rgb(colors[0])
        end = hex_to_rgb(colors[-1])

        response = {
            'rgb': rgb_list_to_hex_list(rgb.interpolate_rgb(begin, end, 1)),
            'hsv': rgb_list_to_hex_list(hsv.interpolate_hsv(begin, end, 1)),
            'lchab': rgb_list_to_hex_list(lchab.interpolate_lchab(begin, end, 1)),
            'lchuv': rgb_list_to_hex_list(lchuv.interpolate_lchuv(begin, end, 1)),
            'lab': rgb_list_to_hex_list(lab.interpolate_lab(begin, end, 1)),
            'xyz': rgb_list_to_hex_list(xyz.interpolate_xyz(begin, end, 1))
        }
        return response

    if new_size == 2:
        response = {
            'rgb': [colors[0], colors[-1]],
            'hsv': [colors[0], colors[-1]],
            'lchab': [colors[0], colors[-1]],
            'lchuv': [colors[0], colors[-1]],
            'lab': [colors[0], colors[-1]],
            'xyz': [colors[0], colors[-1]]
        }
        return response

    if original_size == new_size:
        response = {
            'rgb': colors,
            'hsv': colors,
            'lchab': colors,
            'lchuv': colors,
            'lab': colors,
            'xyz': colors
        }

        return response

    # main logic
    # calculate how many steps we need to add between each color
    # formula: a + (a - 1)x = b + (b - 1)y
    # where a is the original size, b is the new size, and x and y are the
    # number of steps between each color
    a_val = original_size
    b_val = new_size

    steps = 0 # the number of steps between each color

    # solve for a positive x and y
    # we know that an integer solution exists
    for x_val in range(1000):
        # calculate if y is an integer
        # rewrite as: a + (a - 1)x - b = (b - 1)y
        value = a_val + (a_val - 1) * x_val - b_val
        if value % (b_val - 1) == 0:
            steps = x_val
            break

    colors = hex_list_to_rgb_list(colors)
    # interpolate between each color with the new steps
    response = {
        'rgb': blend_palette_helper(rgb.interpolate_rgb, colors, steps, new_size),
        'hsv': blend_palette_helper(hsv.interpolate_hsv, colors, steps, new_size),
        'lchab': blend_palette_helper(lchab.interpolate_lchab, colors, steps, new_size),
        'lchuv': blend_palette_helper(lchuv.interpolate_lchuv, colors, steps, new_size),
        'lab': blend_palette_helper(lab.interpolate_lab, colors, steps, new_size),
        'xyz': blend_palette_helper(xyz.interpolate_xyz, colors, steps, new_size)
    }

    return response




@api_bp.route('/color_lerp', methods=['POST'])
def color_lerp():
    """The color lerp API."""
    data = request.json

    colors = data['colors']
    new_size = int(data['new_size'])

    colors = blend_palette(colors, new_size)
    return colors
