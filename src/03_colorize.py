from pathlib import Path

import matplotlib.pyplot as plt
import skimage.io as io

plt.rcParams["font.family"] = "IBM Plex Sans"
pattern_cropped_adjusted = io.imread("images/pattern_cropped_adjusted.tif")
cm_to_inches = 0.3937008
height_cm = 24
width_cm = 17 * 2 + 1.4
fig, ax = plt.subplots(figsize=(width_cm * cm_to_inches, height_cm * cm_to_inches))

dpi = 1200


ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=37.5, vmax=235)
ax.axis("off")

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

Path(f"images/{dpi}dpi").mkdir(exist_ok=True)

whitespace = 0.5 * cm_to_inches

fig.savefig(
    f"images/{dpi}dpi/pattern_cropped_adjusted_viridis_annotated_{dpi}dpi.png",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=0,
)
fig.savefig(
    f"images/{dpi}dpi/pattern_cropped_adjusted_viridis_annotated_{dpi}dpi_whitespace.png",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=whitespace,
)
fig.savefig(
    f"images/{dpi}dpi/pattern_cropped_adjusted_viridis_annotated_{dpi}dpi.pdf",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=0,
)
fig.savefig(
    f"images/{dpi}dpi/pattern_cropped_adjusted_viridis_annotated_{dpi}dpi_whitespace.pdf",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=whitespace,
)
