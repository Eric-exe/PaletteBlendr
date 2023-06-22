"""Displays RGB interpolation as a series of rectangles in matplotlib."""

import matplotlib.pyplot as plt
from src.color_lerp.rgb import interpolate_rgb
from src.color_lerp.hsv import interpolate_hsv
from src.color_lerp.lchab import interpolate_lchab
from src.color_lerp.lchuv import interpolate_lchuv
from src.color_lerp.lab import interpolate_lab
from src.color_lerp.xyz import interpolate_xyz

# Define the colors to interpolate between
color_start = (255, 0, 0)
color_end = (0, 0, 255)

STEPS = 15

colors_rgb = interpolate_rgb(color_start, color_end, STEPS)
colors_hsv = interpolate_hsv(color_start, color_end, STEPS)
colors_lchab = interpolate_lchab(color_start, color_end, STEPS)
colors_lchuv = interpolate_lchuv(color_start, color_end, STEPS)
colors_lab = interpolate_lab(color_start, color_end, STEPS)
colors_xyz = interpolate_xyz(color_start, color_end, STEPS)

fig, (
    ax_rgb,
    ax_hsv,
    ax_lchuv,
    ax_lchab,
    ax_lab,
    ax_xyz
    ) = plt.subplots(nrows=6, constrained_layout=True)

def plot_colors(colors, axis, title):
    """Plots a list of colors as a series of rectangles in matplotlib."""
    for i, color in enumerate(colors):
        rect = plt.Rectangle((i + 0.1, 0.1), 0.8, 0.8, color=[c / 255 for c in color])
        axis.add_patch(rect)

    axis.set_xlim([0, len(colors)])
    axis.set_ylim([0, 1])
    axis.set_xticks([])
    axis.set_yticks([])
    axis.spines['top'].set_visible(False)
    axis.spines['bottom'].set_visible(False)
    axis.spines['left'].set_visible(False)
    axis.spines['right'].set_visible(False)
    title_obj = axis.set_ylabel(title, rotation='horizontal', ha='right')
    title_obj.set_verticalalignment('center')
    axis.set_aspect('equal')

plot_colors(colors_rgb, ax_rgb, 'RGB')
plot_colors(colors_hsv, ax_hsv, 'HSV')
plot_colors(colors_lchab, ax_lchab, 'LCHab')
plot_colors(colors_lchuv, ax_lchuv, 'LCHuv')
plot_colors(colors_lab, ax_lab, 'LAB')
plot_colors(colors_xyz, ax_xyz, 'XYZ')

plt.show()
