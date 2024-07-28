import matplotlib.pyplot as plt
import numpy as np
import skimage as ski
import skimage.io as io

# paper size settings
height_cm = 24
width_cm = 17 * 2 + 1

# read in pattern
pattern_raw = np.rot90(io.imread("pattern_raw.tif"))
(height_raw, width_raw) = pattern_raw.shape
print(pattern_raw.shape)

# crop to desired size
crop_tb = 500
height_cropped = height_raw - crop_tb
width_cropped = int(height_cropped * (width_cm / height_cm))
print(width_cropped)
pattern_cropped = pattern_raw[crop_tb // 2 : height_cropped, 0:width_cropped]

# cut outliers in intensity
median_int = np.median(pattern_cropped)
pattern_cropped[pattern_cropped > 3 * median_int] = 3 * median_int

# save results
io.imsave("pattern_cropped.tif", pattern_cropped)
io.imshow(pattern_cropped)
plt.show()
