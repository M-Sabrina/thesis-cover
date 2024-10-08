from pathlib import Path

import matplotlib.pyplot as plt
import skimage.io as io

plt.rcParams["font.family"] = "IBM Plex Sans"
pattern_cropped_adjusted = io.imread("images/pattern_cropped_adjusted.tif")
cm_to_inches = 0.3937008
height_cm = 25
width_cm = 17 * 2 + 2.5
fig, ax = plt.subplots(figsize=(width_cm * cm_to_inches, height_cm * cm_to_inches))

dpi = 600

ax.imshow(pattern_cropped_adjusted, cmap="viridis", vmin=37.5, vmax=235)
ax.axis("off")

fontcolor = "white"

(height, width) = pattern_cropped_adjusted.shape
ax.text(
    width // 2 + 320,
    height // 4 + 200,
    "    Spiraling Towards Understanding\n In Vitro Min Protein Surface Patterns",
    fontsize=20,
    va="top",
    color=fontcolor,
)
ax.text(
    width // 2 + 790,
    3 * height // 4,
    " Sabrina C. M. Meindlhumer",
    fontsize=19,
    va="top",
    color=fontcolor,
    style="oblique",
)
ax.text(
    width // 2 - 50,
    250,
    "  Spiraling Towards Understanding In Vitro Min Protein Surface Patterns  |  Sabrina C. M. Meindlhumer",
    fontsize=9.7,
    va="top",
    color=fontcolor,
    rotation=270,
    weight="bold",
)

fig.canvas.draw()

outpath = Path(f"images/{dpi}dpi")
Path(outpath).mkdir(exist_ok=True)

whitespace = 0.5 * cm_to_inches

fig.savefig(
    outpath
    / f"pattern_cropped_adjusted_viridis_annotated_height{int(height_cm*10)}mm_width{int(width_cm*10)}mm_{dpi}dpi_schoone_maat.pdf",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=0,
)
fig.savefig(
    outpath
    / f"pattern_cropped_adjusted_viridis_annotated_height{int(height_cm*10)}mm_width{int(width_cm*10)}mm_{dpi}dpi_plus_5mm_whitespace.pdf",
    dpi=dpi,
    bbox_inches="tight",
    pad_inches=whitespace,
)
