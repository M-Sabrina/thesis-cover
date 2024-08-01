import matplotlib.pyplot as plt
import numpy as np
import skimage.io as io

pattern_cropped_adjusted = io.imread("images/pattern_cropped_adjusted.tif")

fig, ax = plt.subplots()

dpi = 1000

# ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=0, vmax=255)
# fig.savefig("images/pattern_cropped_adjusted_viridis_vs1.png", dpi=dpi)

# ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=25, vmax=230)
# fig.savefig("images/pattern_cropped_adjusted_viridis_vs2.png", dpi=dpi)

# ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=50, vmax=230)
# fig.savefig("images/pattern_cropped_adjusted_viridis_vs3.png", dpi=dpi)

# ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=75, vmax=255)
# fig.savefig("images/pattern_cropped_adjusted_viridis_vs4.png", dpi=dpi)

# ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=25, vmax=255)
# fig.savefig("images/pattern_cropped_adjusted_viridis_vs5.png", dpi=dpi)

# ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=0, vmax=235)
# fig.savefig("images/pattern_cropped_adjusted_viridis_vs6.png", dpi=dpi)

# ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=37.5, vmax=230)
# fig.savefig("images/pattern_cropped_adjusted_viridis_vs7.png", dpi=dpi)

# ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=50, vmax=255)
# fig.savefig("images/pattern_cropped_adjusted_viridis_vs8.png", dpi=dpi)

ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=37.5, vmax=235)
ax.axis("off")
fig.savefig(
    "images/pattern_cropped_adjusted_viridis.png",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=0,
)
ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=37.5, vmax=235)
ax.axis("off")


(height, width) = pattern_cropped_adjusted.shape
ax.text(
    2 * width // 3 - 600,
    height // 4 + 200,
    "  Spiraling Towards Understanding\nIn Vitro Min Protein Surface Patterns",
    fontsize=6,
    va="top",
    color="white",
)
ax.text(
    2 * width // 3 - 350,
    3 * height // 4,
    "Sabrina C. M. Meindlhumer",
    fontsize=6,
    va="top",
    color="white",
)
fig.canvas.draw()
fig.savefig(
    "images/pattern_cropped_adjusted_viridis_annotated.png",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=0,
)
