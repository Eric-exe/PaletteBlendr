"""Displays RGB interpolation as a series of rectangles in matplotlib."""

import matplotlib.pyplot as plt
from src.color_lerp.hsv import interpolate_hsv_steps

# Define the colors to interpolate between
color_start = (255, 0, 0)
color_end = (0, 0, 255)
colors = interpolate_hsv_steps(color_start, color_end, 4)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot a rectangle for each color
for i, color in enumerate(colors):
    rect = plt.Rectangle((i, 0), 1, 1, color=[c/255 for c in color])
    # normalize the color values to be between 0 and 1 so matplotlib can understand them

    ax.add_patch(rect)

# Set the axis limits and labels
ax.set_xlim([0, len(colors)])
ax.set_ylim([0, 1])
ax.set_xticks([])
ax.set_yticks([])

# Show the plot
plt.show()
