import matplotlib.pyplot as plt
import skimage.io as io

plt.rcParams["font.family"] = "IBM Plex Sans"
pattern_cropped_adjusted = io.imread("images/pattern_cropped_adjusted.tif")

fig, ax = plt.subplots()

dpi = 300

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
# fig.savefig(
#     "images/pattern_cropped_adjusted_viridis.png",
#     dpi=dpi,
#     bbox_inches="tight",
#     pad_inches=0,
# )

# fontcolor = "#ffedd5"
fontcolor = "white"

(height, width) = pattern_cropped_adjusted.shape
ax.text(
    width // 2 + 300,
    height // 4 + 200,
    "    Spiraling Towards Understanding\n In Vitro Min Protein Surface Patterns",
    fontsize=9,
    va="top",
    color=fontcolor,
)
ax.text(
    width // 2 + 700,
    3 * height // 4,
    " Sabrina C. M. Meindlhumer",
    fontsize=9,
    va="top",
    color=fontcolor,
    style="oblique",
)
ax.text(
    width // 2 - 30,
    275,
    "  Spiraling Towards Understanding In Vitro Min Protein Surface Patterns  |  Sabrina C. M. Meindlhumer",
    fontsize=4.3,
    va="top",
    color=fontcolor,
    rotation=270,
    weight="bold",
)
fig.canvas.draw()
fig.savefig(
    f"images/pattern_cropped_adjusted_viridis_annotated_{dpi}dpi.png",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=0,
)
