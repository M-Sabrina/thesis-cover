import numpy as np
import skimage as ski
import skimage.io as io

pattern_cropped = io.imread("images/pattern_cropped.tif")


# improve with contrast
pattern_cropped_adjusted = ski.exposure.adjust_gamma(pattern_cropped).astype(np.uint8)

io.imsave("images/pattern_cropped_adjusted.tif", pattern_cropped_adjusted)
